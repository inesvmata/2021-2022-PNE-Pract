
import http.client
import json
import termcolor
from clientclass import Client
IP = "127.0.0.1"
PORT = 8081
c = Client(IP, PORT)

def make_ensembl_request(endpoint,parameter):
    #SERVER = 'rest.ensembl.org'
    #PARAMS = '?content-type=application/json'

    conn = http.client.HTTPConnection(IP, PORT)
    try:
        conn.request("GET", endpoint + parameter)
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

#ADVANCED LEVEL
listSpecies = make_ensembl_request("/listSpecies?","limit=8&json=1")
print("List of species: ")
print(listSpecies)

karyotype = make_ensembl_request("/karyotype?","specie=human&json=1")
print("karyotype")
print(karyotype)

chromosome_length = make_ensembl_request("/chromosomeLength?","specie=human&chromosome=9&json=1")
print("Chromosome length:")
print(chromosome_length)

geneSeq = make_ensembl_request("/geneSeq?","gene=FRAT1&json=1")
print("Sequence of the human gene:")
print(geneSeq)

geneInfo = make_ensembl_request("/geneInfo?","info=FRAT1&json=1")
print("Information about the gene:")
print(geneInfo)

geneCalc = make_ensembl_request("/geneCalc?","calculation=FRAT1&json=1")
print("Calculations on the gene:")
print(geneCalc)

geneList = make_ensembl_request("/geneList?","specie=human&chromo=9&start=22125500&end=22136000&json=1")
print("Names of the genes in the given range:")
print(geneList)