from Seq1 import Seq
seq1 = Seq("")
seq2 = Seq("ACTGA")
seq3 = Seq("Invalid sequence")
print(f"Sequence : (Length: {seq1.new_len()}) {seq1}")
print(f"Sequence : (Length: {seq2.len()}) {seq2}")
print(f"Sequence : (Length: {seq3.new_len()}) {seq3}")