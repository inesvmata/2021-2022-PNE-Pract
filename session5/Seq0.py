def seq_ping():
    print("OK!")

def seq_len(sequence):
    count_A = 0
    count_C = 0
    count_G = 0
    count_T = 0
    for i in sequence:
        if i == "A":
            count_A += 1
        elif i == "C":
            count_C += 1
        elif i == "G":
            count_G += 1
        elif i == "T":
            count_T += 1
    return count_A, count_C, count_G, count_T