from client import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
#EXERCISE 1
print("TESTING PING...")
response = c.talk("PING")
print(response)

#EXERCISE 2
list_get = ["GET 0", "GET 1", "GET 2", "GET 3", "GET4"]
for e in list_get:
    print("TESTING", e, "...")
    response = c.talk(e)
    print(response)

#EXERCISE 3
print("TESTING INFO...")
response = c.talk("INFO AACCGGGTTT")
print(response)

#EXERCISE 4
print("TESTING COMP...")
response = c.talk("COMP AACCGGGTTT")
print(response)

#EXERCISE 5
print("TESTING REV...")
response = c.talk("REV AACCGGGTTT")
print(response)

#EXERCISE 6
print("TESTING GENE...")
list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for g in list_genes:
    print("TESTING", g, "...")
    response = c.talk(g)
    print(response)



# -- Print the IP and PORTs
print(f"IP: {c.ip}, {c.port}")