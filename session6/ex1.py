from firstclass import Seq

#st1 = "ACCTGC"
#st2 = "Hello? Am I a valid sequence?"
str_list = ["ACCTGC", "Hello? Am I a valid sequence?"]
sequence_list = []
#s1 = s.Seq("ACCTGC")
#s2 = s.Seq("Hello? Am I a valid sequence?")
#print(f"Sequence 1: {s1}")
#print(f"Sequence 2: {s2}")
for st in str_list:
    if Seq.valid_sequence2(st):
        #si usas strings como argumentos, no puedes usar una function con class, tienes que usar un static method
        sequence_list.append(Seq(st))
    else:
        sequence_list.append(Seq("ERROR"))

for i in range(0, len(sequence_list)):
    print("Sequence", str(i) + ":", sequence_list[i])


