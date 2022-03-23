import socket

class Client:
   def __init__(self, ip, port):
       self.ip = ip
       self.port = port

   def ping(self):
       print("OK!!!!")

   def __str__(self):
       return "Connection to SERVER at " + str(self.ip) + ", PORT: " + str(self.port)

   def talk(self, msg):
       # -- Create the socket
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

       # establish the connection to the Server (IP, PORT)
       s.connect((self.ip, self.port))

       # Send data.
       s.send(str.encode(msg))

       # Receive data
       response = s.recv(2048).decode("utf-8")

       # Close the socket
       s.close()

       # Return the response
       return response

class Seq():
    def __init__(self, strbases="NULL"):
        self.strbases = strbases
        if strbases == "NULL":
            print("NULL sequence created")
            self.strbases = "NULL"
        elif not self.valid_sequence():
            print("INVALID Seq!")
            self.strbases = "ERROR"
        else:
            print("New sequence created!")
            self.strbases = strbases

    def valid_sequence(self): #as this function belongs to Seq class, we have to write it below the init method
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def __str__(self):
        return self.strbases

    def seq_read_fasta(self, filename):
        f = open("../P0/" + "./sequences/" + filename, "r").read()
        self.strbases = f[f.find("\n"):].replace("\n", "")
        return self.strbases