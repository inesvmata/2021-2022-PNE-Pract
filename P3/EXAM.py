from clientseqclasses import Client

PRACTICE = 3
EXERCISE = "EXAM"

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
response = c.talk("OPE ACGT")
print(response)


# -- Print the IP and PORTs
print(f"IP: {c.ip}, {c.port}")