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
        print(len(seq_read_fasta(l[0])))
        print(len(seq_read_fasta(l[1])))
        print(len(seq_read_fasta(l[2])))
        print(len(seq_read_fasta(l[3])))
        print(len(seq_read_fasta(l[4])))




