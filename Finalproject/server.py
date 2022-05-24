import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
import http.client
import json


LIST_SEQUENCES = ["AAAGGGCCCTTTT", "AGGGCCCTT", "GGGTTTCCCAAA", "TTTAAAGGGAAACCCC", "GGTTAACCCTTAAGGAAAA", "AAGGGTTTCCCC"]
LIST_GENES = ["ADA", "FRAT1", "FXN", "RNU5A", "U5"]


def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents


def seq_count(sequence):
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for i in sequence:
        d[i] += 1
    total = sum(d.values())
    for k, v in d.items():
        d[k] = [v, (v * 100) / total]
    return d


def convert_message(base_count):
    message = ""
    for k, v in base_count.items():
        message += k + ":" + str(v[0]) + " (" + str(round(v[1], 2)) + "%)" + "\n"
    return message


def info_operation(arg):
    base_count = seq_count(arg)
    response = "Sequence: " + arg + "\n"
    response += "Total length: " + str(len(arg)) + "\n"
    response += convert_message(base_count)
    return response

def seq_complement(sequence):
    d = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement = ""
    for i in sequence:
        new_bases = d[i]
        complement += new_bases
    return complement



# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

def request_json(endpoint, parameter):
    SERVER = 'rest.ensembl.org'
    PARAMS = '?content-type=application/json'

    print(f"\nServer: {SERVER}")

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)

    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", endpoint + parameter + PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)  # to transform it to a dictionary, it transforms the data into its corresponding type.
    print(data1)

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)


        print(arguments)
        print("The new path is", url_path.path) #these paths have all different paths

        if path == "/":
            contents = read_html_file("index.html").render(context={})
        elif path == "/species":
            ENDPOINT = 'info/species'
            Species = request_json(ENDPOINT, "")
            species = Species["species"]
            try:
                name_species = []
                limit = int(arguments["limit"][0])
                for i in range(0, limit):
                    name_species.append(species[i]["display_name"])
                contents = read_html_file(path[1:] + ".html").render(context={"species": name_species, "n_species": len(name_species), "limit": limit})
            except Exception:
                contents = read_html_file("ERROR.html").render()



        else:
            contents = read_html_file("ERROR.html").render()

        # Open the form1.html file
        # Read the index from the file
        #contents = Path('form-1.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()