def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:
        d[b] += 1
    return d

with open("sequences.txt", "r") as f:
    sequences = f.readlines()
    for seq in sequences:
        new_seq = seq.replace("\n", "")
        print("Total length", len(new_seq))
        for k, v in count_bases(new_seq).items():
            print(k + ":", v)

dna_seq = input("Introduce the sequence: ")
print("Total length:", len(dna_seq))
print(count_bases(dna_seq))
for k, v in count_bases(dna_seq).items(): #.items() imprime los values de un diccionario
    print(k + ":", v)
