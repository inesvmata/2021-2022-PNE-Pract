from Seq1 import Seq
seq1 = Seq()
seq2 = Seq("ACTGA")
seq3 = Seq("Invalid sequence")
print(f"Sequence : (Length: {seq1.new_len()}) {seq1}")
print("Bases: ", seq1.seq_count())
print("Reverse: ", seq1.seq_reverse())
print("Complement: ", seq1.seq_complement())
print(f"Sequence : (Length: {seq2.len()}) {seq2}")
print("Bases: ", seq2.seq_count())
print("Reverse: ", seq2.seq_reverse())
print("Complement: ", seq2.seq_complement())
print(f"Sequence : (Length: {seq3.new_len()}) {seq3}")
print("Bases: ", seq3.seq_count())
print("Reverse: ", seq3.seq_reverse())
print("Complement: ", seq3.seq_complement())