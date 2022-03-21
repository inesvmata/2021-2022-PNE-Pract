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
    def __init__(self,strbases="NULL"):
        self.strbases = strbases
        if not self.valid_sequence():
            self.strbases = "ERROR"
            print("INVALID sequence created!!!!")
        elif self.strbases == "":
            self.strbases = "NULL"
            print("NULL sequence created!")
        else:
            print("New sequence created!")

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
    def len(self):
        return len(self.strbases)

    def new_len(self):
        new_len = ""
        if self.strbases == "ERROR" or self.strbases == "NULL":
            return len(new_len)

    def count_base(self):
        count_C = 0
        count_G = 0
        count_T = 0
        count_A = 0
        for i in self.strbases:
            if i == "C":
                count_C += 1
            elif i == "G":
                count_G += 1
            elif i == "T":
                count_T += 1
            elif i == "A":
                count_A += 1
        return count_C, count_G, count_T, count_A

    def count_base2(self, strbases="NULL"):
        count_C = 0
        count_G = 0
        count_T = 0
        count_A = 0
        new_len = ""
        if self.strbases == "ERROR" or self.strbases == "NULL":
            for i in new_len:
                if i == "C":
                    count_C += 1
                elif i == "G":
                    count_G += 1
                elif i == "T":
                    count_T += 1
                elif i == "A":
                    count_A += 1
        return count_C, count_G, count_T, count_A



    def seq_count(self):
        d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        if self.strbases == "ERROR" or self.strbases == "NULL":
            return d
        else:
            for i in self.strbases:
                d[i] += 1
                total = sum(d.values())
                for k,v in d.items():
                    d[k] = [v, (v * 100) / total]
        return d

    def convert_message(self, base_count):
        message = ""
        for k, v in base_count.items():
            message += k + ":" + str(v[0]) + " (" + str(v[1]) + "%)" + "\n"
        return message

    def info_operation(self, arg):
        base_count = self.seq_count()
        response = "Sequence: " + arg + "\n"
        response += "Total length: " + str(len(arg)) + "\n"
        response += self.convert_message(base_count)
        return response

    def seq_reverse(self):
        reverse = []
        if self.strbases == "ERROR" or self.strbases == "NULL":
            reverse = self.strbases
        else:
            for i in self.strbases:
                reverse = self.strbases[::-1]
        return reverse

    def seq_complement(self):
        d = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        complement = ""
        if self.strbases == "ERROR" or self.strbases == "NULL":
            complement = self.strbases
        else:
            for i in self.strbases:
                new_bases = d[i]
                complement += new_bases
        return complement

