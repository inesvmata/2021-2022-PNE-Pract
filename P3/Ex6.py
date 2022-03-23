from clientseqclasses import Client

PRACTICE = 3
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
#response = c.talk("GENE U5")
#print(response)

list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for g in list_genes:
    response = c.talk("GENE " + str(g))
    print( "Gene", g, ":", response)


# -- Print the IP and PORTs
print(f"IP: {c.ip}, {c.port}")