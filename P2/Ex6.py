from Client0 import Client

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT1 = 8081
PORT2 = 8082

# -- Create a client object
c1 = Client(IP, PORT1)
print(c1)
c2 = Client(IP, PORT2)

...
# -- Send a message to the server
from Client0 import Seq
s = Seq()
print("Sending the FRAT1 gene to the server in fragments of 10 bases....")
gene = s.seq_read_fasta("FRAT1")
print("Gene FRAT1: ", gene)
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
    f6 = gene[50:59]
    f7 = gene[60:69]
    f8 = gene[70:79]
    f9 = gene[80:89]
    f10 = gene[90:99]

print("Fragment 1: ", f1)
print("Fragment 2: ", f2)
print("Fragment 3: ", f3)
print("Fragment 4: ", f4)
print("Fragment 5: ", f5)
print("Fragment 6: ", f6)
print("Fragment 7: ", f7)
print("Fragment 8: ", f8)
print("Fragment 9: ", f9)
print("Fragment 10: ", f10)



list_fragments1 = [f1, f3, f5, f7, f9]
for f in list_fragments1:
    response1 = c1.talk(f)

list_fragments2 = [f2, f4, f6, f8, f10]
for f in list_fragments2:
    response2 = c2.talk(f)

print(f"Response: {response1}")
print(f"Response: {response2}")
...
