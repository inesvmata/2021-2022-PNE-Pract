from client import Client

PRACTICE = 3
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
c.talk("GET 1")
response = c.talk("GET 1")
print(response)


# -- Print the IP and PORTs
print(f"IP: {c.ip}, {c.port}")