import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse


#HTML_FOLDER = "/"
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
            contents = read_html_file("index.html").render(context={"n_sequence": len(LIST_SEQUENCES), "genes": LIST_GENES})

        elif path == "/ping":
            contents = read_html_file(path[1:] + ".html").render() #THIS IS HOW TO EXTRACT THE FILENAME

        elif path == "/get":
            n_sequence = int(arguments["n_sequence"][0]) #this is always going to be an integer
            #&number = value
            #params = "&number=" + str(n_sequence)
            #ensembl_answer = make_call("/sequence/id", params)
            sequence = LIST_SEQUENCES[n_sequence]
            contents = read_html_file(path[1:] + ".html").render(context={"n_sequence": n_sequence, "sequence": sequence})

        elif path == "/gene":
            gene_name = arguments["genes"][0]
            sequence = Path("./sequences/" + gene_name).read_text()
            sequence = sequence[sequence.find("\n"):].replace("\n", "")
            contents = read_html_file(path[1:] + ".html").render(context={"gene_name": gene_name, "sequence": sequence})

        elif path == "/operation":
            sequence = arguments["sequence"][0]
            operation = arguments["operation"][0]
            if operation == "rev":
                contents = read_html_file(path[1:] + ".html").render(context={"sequence": sequence, "operation": operation, "result": sequence[::-1]})
            elif operation == "info":
                contents = read_html_file(path[1:] + ".html").render(context={"sequence": sequence, "operation": operation, "result": info_operation(sequence)})
            elif operation == "comp":
                contents = read_html_file(path[1:] + ".html").render(
                    context={"sequence": sequence, "operation": operation, "result": seq_complement(sequence)})



        else:
            contents = Path("ERROR.html").read_text()

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