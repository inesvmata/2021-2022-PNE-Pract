class Seq:
    "A class for representing sequences"
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

    def len(self):
        return len(self.strbases)
    def seq_read_fasta(self, filename):
        f = open("./sequences/" + filename, "r").read()
        self.strbases = f[f.find("\n"):].replace("\n", "")