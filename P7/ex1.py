# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
#params should be &param1=a
PARAMS = '?content-type=application/json'
#URL = SERVER + ENDPOINT + PARAMS

print(f"\nConnecting to server: {SERVER}\n")
#print(f"URL: {URL}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMS)
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

# -- Print the received data
print(f"CONTENT: {data1}") #type(data1["ping"]) is an integer number, because json has transformed it into an integer.
if data1["ping"] == 1: #no poner "1".
    print("PING OK!!!! The database is running.")
else:
    print("ERROR!!!! The database is not running.")