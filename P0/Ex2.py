filename = Seq0.valid_filename()
sequence = Seq0.seq_read_fasta(filename)
print("The first 20 bases are: ", sequence[:20])