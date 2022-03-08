import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 8080
IP = "localhost"


# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))


# Closing the socket
s.close()

#si te sale el error address already used significa que ya tienes un server running en ese port en el mismo ordenador.
#puedes derun un server y run el otro o usar esta función:
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)