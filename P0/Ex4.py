import Seq0
filename = Seq0.valid_filename()
sequence = Seq0.seq_read_fasta(filename)
count_C, count_G, count_T, count_A = Seq0.seq_count_base(sequence)
print("Gene", filename)
print("A: ",count_A, "\nC: ", count_C, "\nG: ", count_G, "\nT: ", count_T)