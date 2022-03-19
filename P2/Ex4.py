from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)
print(c)

...
# -- Send a message to the server
from Client0 import Seq
s = Seq()
list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for l in list_genes:
    print("Sending the", l, "gene to the server...")
    gene = str(s.seq_read_fasta(l))
    response = c.talk(gene)
    print(f"Response: {response}")
...
