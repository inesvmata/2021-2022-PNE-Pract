import Seq0
filename = Seq0.valid_filename()
sequence = Seq0.seq_read_fasta(filename)
fragment = sequence[:20]
complement = Seq0.seq_complement(fragment)
print("Fragment:", fragment)
print("Complement:", complement)
