# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json
from Seqclass import Seq


genes_dict = {"SRCAP": "ENSG00000080603",
              "FRAT1": "ENSG00000165879",
              "ADA": "ENSG00000196839",
              "FXN": "ENSG00000165060",
              "RNU6_269P": "ENSG00000212379",
              "MIR633": "ENSG00000207552" ,
              "TTTY4C": "ENSG00000228296" ,
              "RBMY2YP": "ENSG00000227633" ,
              "FGFR3": "ENSG00000068078" ,
              "KDR": "ENSG00000128052",
              "ANK2": "ENSG00000145362"}

GENE = input("Enter a gene: ")
SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id'
PARAMS = '?content-type=application/json'
URL = ENDPOINT + "/" + genes_dict[GENE] + PARAMS

print(f"\nServer: {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", URL)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")
data1 = json.loads(data1) #to transform it to a dictionary, it transforms the data into its corresponding type.
print(data1)

print("Gene: -->", GENE)
print("Description: -->", data1['desc']) #ERROR
print("Sequence: -->", data1['seq'])
s = data1['seq']
seq = Seq(s)
print("Total length: -->", Seq.len(seq))
#print(str(Seq.info_operation(seq)))
#base_count = Seq.seq_count(seq)
#print(Seq.convert_message(base_count))
# -- Print the received data
#print(f"CONTENT: {data1}") #type(data1["ping"]) is an integer number, because json has transformed it into an integer.
