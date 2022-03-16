from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

...
# -- Send a message to the server
FILENAME = input("Enter a filename: ")
print("Sending the", FILENAME, "gene to the server...")
response = c.seq_read_fasta(FILENAME)

print(f"Response: {response}")
...
