from Seq1 import Seq
list_genes = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
for l in list_genes:
    s = Seq()
    sequence = s.seq_read_fasta(l)
    count_C, count_G, count_T, count_A = sequence.count_base()
    max_base = sequence.max_base(count_C, count_G, count_T, count_A, sequence)
print("Gene", l)
print("Most frequent base:", max_base)
