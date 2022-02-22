import Seq0
filename = Seq0.valid_filename()
sequence = Seq0.seq_read_fasta(filename)
b_dict = Seq0.seq_count(sequence)
print("Gene", filename, ":", b_dict)