import Seq0
filename = Seq0.valid_filename()
sequence = Seq0.seq_read_fasta(filename)
frag, reverse = Seq0.seq_reverse(sequence)
print("Gene", filename)
print("Fragment: ", frag)
print("Reverse: ", reverse)
