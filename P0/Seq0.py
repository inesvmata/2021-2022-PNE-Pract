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
    import Seq0
    FOLDER = "./sequences/"
    list_genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
    for l in list_genes:
        print(len(Seq0.seq_read_fasta(l))) #ponerlo solo una vez pq ya tienes el for loop q hace el len para todas las listas

#def seq_count_base():
    #d = {"U5": "", "FRAT1": "", "ADA": "", "FXN": "", "RNU6_269P": ""}
    #for gene in d:
        #gene_U5 = seq_read_fasta(gene[0])
        #gene_FRAT1 = seq_read_fasta(gene[1])
        #gene_ADA = seq_read_fasta(gene[2])
        #gene_FXN = seq_read_fasta(gene[3])
        #gene_RNU6_269P = seq_read_fasta(gene[4])
        

