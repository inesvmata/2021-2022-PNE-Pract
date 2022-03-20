import socket
import Seqclass

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

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
    msg = msg_raw.decode().replace("\n", "").strip()  # usually the server recieves msg\n, so we have to eliminate the end of line space
    cmd = msg.split(' ')[0]
    print(cmd)
    # -- Print the received message
    if cmd != "PING":
        arg = msg.split(' ')[1]
        print(arg)
    print(f"Message received: {msg}")

    # -- Manage message
    if cmd == "PING":
        response = "OK!\n"
        print("PING command!")

    elif cmd == "REV":
        response = arg[::-1]

    elif cmd == "INFO":
        base_count = Seqclass.count_base(arg)
        response = "Sequence: " + arg + "\n"
        response += "Total length: " + str(len(arg)) + "\n"


    else:
        response = "This command is not available in the server.\n"


    # -- The message has to be encoded into bytes
    cs.send(response.encode())

    # -- Close the data socket
    cs.close()