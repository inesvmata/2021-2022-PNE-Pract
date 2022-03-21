from client import Client

PRACTICE = 3
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
c.talk("PING")
response = c.talk("PING")
print(response)


# -- Print the IP and PORTs
print(f"IP: {c.ip}, {c.port}")