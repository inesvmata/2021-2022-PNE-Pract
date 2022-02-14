import Seq0
filename = Seq0.valid_filename()
sequence = Seq0.seq_read_fasta(filename)
len_seq = Seq0.seq_len(sequence)