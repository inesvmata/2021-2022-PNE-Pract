from Seq1 import Seq
s = Seq()
FILENAME = input("Enter a filename: ")
s.seq_read_fasta(FILENAME)
print(f"Sequence : (Length: {s.len()}) {s}")
print("Bases: ", s.seq_count())
print("Reverse: ", s.seq_reverse())
print("Complement: ", s.seq_complement())