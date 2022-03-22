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
list_get = ["GET 0", "GET 1", "GET 2", "GET 3", "GET4"]
for e in list_get:
    print("TESTING", e)
    response = c.talk(e)
    print(response)



# -- Print the IP and PORTs
print(f"IP: {c.ip}, {c.port}")