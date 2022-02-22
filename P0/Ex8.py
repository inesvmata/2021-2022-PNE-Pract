import Seq0
filename = Seq0.valid_filename()
sequence = Seq0.seq_read_fasta(filename)
count_C, count_G, count_T, count_A = Seq0.seq_count_base(sequence)
max_base = Seq0.max_base(count_C, count_G, count_T, count_A, sequence)
print("Gene", filename)
print("Most frequent base:", max_base)
