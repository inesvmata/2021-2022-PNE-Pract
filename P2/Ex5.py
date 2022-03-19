from Client0 import Client

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 21000

# -- Create a client object
c = Client(IP, PORT)
print(c)

...
# -- Send a message to the server
from Client0 import Seq
s = Seq()
print("Sending the FRAT1 gene to the server in fragments of 10 bases....")
gene = s.seq_read_fasta("FRAT1")
f1 = ""
f2 = ""
f3 = ""
f4 = ""
f5 = ""
list_fragments = []
for i in gene:
    f1 = gene[0:9]
    f2 = gene[10:19]
    f3 = gene[20:29]
    f4 = gene[30:39]
    f5 = gene[40:49]

list_fragments = [f1, f2, f3, f4, f5]
for f in list_fragments:
    response = c.talk(f)

print(f"Response: {response}")
...
