import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
import http.client
import json
from Seqclass import Seq

SERVER = 'rest.ensembl.org'
PARAMS = '?content-type=application/json'
GENES = {"FRAT1": "ENSG00000165879",
             "ADA": "ENSG00000196839",
             "FXN": "ENSG00000165060",
             "RNU6_269P": "ENSG00000212379",
             "MIR633": "ENSG00000207552",
             "TTTY4C": "ENSG00000228296",
             "RBMY2YP": "ENSG00000227633",
             "FGFR3": "ENSG00000068078",
             "KDR": "ENSG00000128052",
             "ANK2": "ENSG00000145362"}


list_names = []
for n in GENES.keys():
    list_names.append(n)


def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents

def make_ensembl_request(endpoint,parameter):
    SERVER = 'rest.ensembl.org'
    PARAMS = '?content-type=application/json'

    print(f"\nServer: {SERVER}")
    conn = http.client.HTTPConnection(SERVER)

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
    answer = json.loads(data1)  # to transform it to a dictionary, it transforms the data into its corresponding type.
    return answer

# Define the Server's port
PORT = 8081


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
            contents = read_html_file("index.html").render(context={"n_names": list_names})

        #BASIC LEVEL
        elif path == "/listSpecies": #si no pone limite, que salgan todas las especies
            answer = make_ensembl_request("/info/species", "")
            s = answer["species"]
            #name_species2 = []
            try:
                name_species = [] #si no pones nada en el limit es un type error
                limit = int(arguments['limit'][0])
                for i in range(0, limit):
                    name_species.append(s[i]["display_name"])
                if "json" in arguments:
                    contents = {"species": name_species, "n_species": len(s), "limit": limit}
                else:
                    contents = read_html_file("species.html").render(context={"species": name_species, "n_species": len(s), "limit": limit})
            except ValueError: #el limit se sale del range
                if "json" in arguments:
                    contents = {"ERROR": "A key error has occurred"}
                else:
                    contents = Path("ERROR.html").read_text()
            except KeyError:
                name_species2 = []
                for i in range(0, len(s)):
                    name_species2.append(s[i]["display_name"])
                if "json" in arguments:
                    contents = {"species": name_species2, "n_species": len(s), "limit": "no limit specified"}
                else:
                    contents = read_html_file("species.html").render(context={"species": name_species2, "n_species": len(s), "limit": "no limit specified"})

        elif path == "/karyotype":
            try:
                species = str(arguments['specie'][0].strip())
                answer = make_ensembl_request("/info/assembly/", species)
                karyotype = answer["karyotype"]
                if "json" in arguments:
                    contents = {"karyotype": karyotype}
                else:
                    contents = read_html_file("karyotype.html").render(context={"karyotype": karyotype})
            except KeyError:
                if "json" in arguments:
                    contents = {"ERROR": "A key error has occurred"}
                else:
                    contents = Path("ERROR.html").read_text()

        elif path == "/chromosomeLength":
            try:
                species = str(arguments['specie'][0].strip())
                answer = make_ensembl_request("/info/assembly/", species)
                chromo = int(arguments["chromosome"][0].strip())
                dictionary = answer["top_level_region"]
                list_chromosome = []
                for i in range(len(dictionary)):
                    list_chromosome.append(dictionary[i]["name"])
                position = list_chromosome.index(str(chromo)) #la posición en la que está ese cromosoma, para de ahí asacr su length
                position2 = dictionary[position]
                length = int(position2["length"])
                if "json" in arguments:
                    contents = {"length": length}
                else:
                    contents = read_html_file(path[1:] + ".html").render(context={"length": length})
            except KeyError:
                if "json" in arguments:
                    contents = {"ERROR": "A key error has occurred"}
                else:
                    contents = Path("ERROR.html").read_text()

        #MEDIUM LEVEL
        elif path == "/geneSeq":
            try:
                gene = str(arguments['gene'][0].strip())
                key = str(GENES[gene]) #no quiero el nombre, quiero el gen
                answer = make_ensembl_request("/sequence/id/", key)
                sequence = str(answer['seq'])
                if "json" in arguments:
                    contents = {"sequence": sequence}
                else:
                    contents = read_html_file(path[1:] + ".html").render(context={"sequence": sequence})
            except KeyError:
                if "json" in arguments:
                    contents = {"ERROR": "A key error has occurred"}
                else:
                    contents = Path("ERROR.html").read_text()

        elif path == "/geneInfo":
            try:
                gene = str(arguments['info'][0].strip()) #EL GENE QUE EL USUARIO MANDA
                key = str(GENES[gene])
                answer = make_ensembl_request("/sequence/id/", key)
                #print(answer)
                chromo_info = answer['desc'].split(":") #está en desc #aquí no queremos la posición 0
                name_chromo = int(chromo_info[2])
                start = int(chromo_info[3])
                end = int(chromo_info[4])
                length = int(end - start)
                id = str(answer['id']) #o id = key
                if "json" in arguments:
                    contents = {"start": start, "end": end, "name_chromo": name_chromo, "length": length, "id": id}
                else:
                    contents = read_html_file(path[1:] + ".html").render(context={"start": start, "end": end, "name_chromo": name_chromo, "length": length, "id": id})
            except KeyError:
                if "json" in arguments:
                    contents = {"ERROR": "A key error has occurred"}
                else:
                    contents = Path("ERROR.html").read_text()

        elif path == "/geneCalc": #CREO QUE SE PONDRÍA ANTES DEL TRY EL GENE Y EL KEY
            try:
                gene = str(arguments['calculation'][0].strip())
                key = str(GENES[gene])
                answer = make_ensembl_request("/sequence/id/", key)
                sequence = str(answer['seq'])
                seq = Seq(sequence)
                calculations = seq.info_operation(sequence)
                if "json" in arguments:
                    contents = {"sequence": sequence, "calculations": calculations}
                else:
                    contents = read_html_file(path[1:] + ".html").render(context={"sequence": sequence, "calculations": calculations})
            except KeyError:
                if "json" in arguments:
                    contents = {"ERROR": "A key error has occurred"}
                else:
                    contents = Path("ERROR.html").read_text()

        elif path == "/geneList":
            try:
                species = str(arguments['specie'][0].strip())
                chromo = str(arguments['chromo'][0].strip())
                start = str(arguments['start'][0].strip())
                end = str(arguments['end'][0].strip())
                region = chromo + ":" + start + "-" + end
                answer = make_ensembl_request("/phenotype/region/", species + "/" + region)
                #print(answer)
                #dentro de phenotype associations
                final_gene = []
                for i in range(0, len(answer)):
                    for o in answer[i]["phenotype_associations"]:
                        if "attributes" in o:
                            if "associated_gene" in o["attributes"]:
                                final_gene.append(o["attributes"]["associated_gene"])
                                #print(final_gene)
                if "json" in arguments:
                    contents = {"gene": final_gene}
                else:
                    contents = read_html_file(path[1:] + ".html").render(context={"gene": final_gene})
            except KeyError:
                if "json" in arguments:
                    contents = {"ERROR": "A key error has occurred"}
                else:
                    contents = Path("ERROR.html").read_text()

        #ADVANCED LEVEL
        else:
            contents = Path("ERROR.html").read_text()




        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        if "json" in arguments.keys():
            contents = json.dumps(contents)
            self.send_header('Content-Type', 'application/json')

        else:
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