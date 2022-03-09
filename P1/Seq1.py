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
    def count_base2(self,strbases="NULL"):
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
                if i == "C":
                    d['C'] += 1
                elif i == "G":
                    d['G'] += 1
                elif i == "T":
                    d['T'] += 1
                elif i == "A":
                    d['A'] += 1
            return d

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

    def seq_read_fasta(self, filename):
        f = open("../P0/" + "./sequences/" + filename, "r").read() #el P0 lo he puesto yo pero no funciona
        self.strbases = f[f.find("\n"):].replace("\n", "")
        return self.strbases
    #def max_gene(self):
        #list_genes = ["C", "G", "T", "A"]
        #list_count = [count_C, count_G, count_T, count_A]
        #list_zipped = zip(list_genes, list_count)

    def max_base(self, count_C, count_G, count_T, count_A, sequence):
        max_base = ""
        for i in sequence:
            if (count_C > count_G) and (count_C > count_T) and (count_C > count_A):
                max_base = "C"
            elif (count_G > count_C) and (count_G > count_T) and (count_G > count_A):
                max_base = "G"
            elif (count_T > count_G) and (count_T > count_C) and (count_T > count_A):
                max_base = "T"
            elif (count_A > count_G) and (count_A > count_T) and (count_A > count_C):
                max_base = "A"
        return max_base
