def seq_ping():
    print("OK")

def valid_filename():
    FOLDER = "./sequences/"
    exit = False
    while not exit:
        filename = input("Enter a filename: ")
        try:
            f = open(FOLDER + filename, "r")
            #f = open(filename, "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("The file does not exist. Provide another file")

def seq_read_fasta(filename):
    FOLDER = "./sequences/"
    seq = open(FOLDER + filename, "r").read()
    seq = seq[seq.find("\n"):].replace("\n","")
    return seq

def seq_len():
    FOLDER = "./sequences/"
    list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
    for l in list_genes:
        print("Length of", l, ":", len(seq_read_fasta(l))) #ponerlo solo una vez pq ya tienes el for loop q hace el len para todas las listas
def seq_count_base(sequence):
    count_C = 0
    count_G = 0
    count_T = 0
    count_A = 0
    for i in sequence:
        if i == "C":
            count_C += 1
        elif i == "G":
            count_G += 1
        elif i == "T":
            count_T += 1
        elif i == "A":
            count_A += 1
    return count_C, count_G, count_T, count_A

def seq_count(sequence):
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for i in sequence:
        if i == "C":
            d['C'] += 1
        elif i == "G":
            d['G'] += 1
        elif i == "T":
            d['T'] += 1
        elif i == "A":
            d['A'] += 1
    return d


def seq_reverse(sequence):
    frag = sequence[:20]
    reverse = []
    for i in frag:
        reverse = frag[::-1]
    return frag, reverse

def seq_complement(fragment):
    d = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement = ""
    for i in fragment:
        new_bases = d[i]
        complement += new_bases
    return complement

def max_base(count_C, count_G, count_T, count_A, sequence):
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








        

