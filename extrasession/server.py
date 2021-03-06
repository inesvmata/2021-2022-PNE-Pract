import socket

def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:
        d[b] += 1

    total = sum(d.values())
    for k,v in d.items():
        d[k] = [v, (v * 100) / total]
    return d

def convert_message(base_count):
    message = ""
    for k,v in base_count.items():
        message  += k + ": " * str(v[0]) +" (" + str(v[1]) + "%)" +"\n"
    return message

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 20500
IP = "0.0.0.0"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")
    (cs, client_ip_port) = ls.accept()

    print("A client has connected to the server!")

    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode().replace("/n", "").strip()
    split_list = msg.split
    cmd = split_list[0]

    if cmd != "PING":
        arg = split_list[1]

    # -- Manage message
    if msg == "PING":
        response = "PING OK!!!!"


    # -- The message has to be encoded into bytes
    cs.send(response.encode())

    # -- Close the data socket
    cs.close()