N = 11
n1 = 0
n2 = 1
print(n1, end=" ")
print(n2, end=" ")
#for loop to change the value of the variables
for i in range(2, N): #we start from 2 because if we start from 0, we will print 13 numbers, because we already have 2 numbers at the beggining
    num = n1 + n2
    print(num, end=" ")
    n1 = n2
    n2 = num #constant is a variable which has a value that never changes
print() #para que cuando lo imprimas no se cree un espacio en blanco con la última línea
