import socket
from client import Seq
import termcolor

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
    # -- Print the received message
    if cmd != "PING":
        arg = msg.split(' ')[1]
    print(f"Message received: {msg}")

    # -- Manage message
    if cmd == "PING":
        response = "OK!\n"
        termcolor.cprint("PING command!", "green")
        print(response)

    elif cmd == "REV":
        response = arg[::-1]

    elif cmd == "COMP":
        termcolor.cprint(cmd, "green")
        response = Seq.seq_complement(arg)
        print(response)

    elif cmd == "INFO":
        termcolor.cprint(cmd, "green")
        response = Seq.info_operation(arg)
        print(response)


    else:
        response = "This command is not available in the server.\n"


    # -- The message has to be encoded into bytes
    cs.send(response.encode())

    # -- Close the data socket
    cs.close()