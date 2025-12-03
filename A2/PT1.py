# EJ1.1
llista = [3, 7, 1, 9, 4]
print("EJ1.1:", llista)

# EJ1.2
noms = ["Anna", "Pau", "Maria", "Joan", "Laia"]
print("EJ1.2 primer:", noms[0])
print("EJ1.2 ultim:", noms[-1])

# EJ1.3
llista2 = [10, 20, 30, 40]
llista2.append(50)
del llista2[0]
print("EJ1.3:", llista2)

# EJ1.4
print("EJ1.4 len llista:", len(llista))
print("EJ1.4 len noms:", len(noms))

# EJ2
list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]
print("EJ2:", list_num.count(7))

# EJ3
list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]
print("EJ3:", sum(list_num))

# EJ4
print("EJ4 max:", max(list_num), "min:", min(list_num))

# EJ5
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
print("EJ5.1 set:", list(set(list_num)))
nova = []
for x in list_num:
    if x not in nova:
        nova.append(x)
print("EJ5.2 ordre:", nova)

# EJ6 
list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]
print("EJ6:", list_num[::-1])

# EJ7 
list_num = [2, 7, 4, 5, 1]
list_num2 = [8, 3, 9, 6, 10]
print("EJ7:", list_num + list_num2)

# EJ8 
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
num = int(input("EJ8 num? "))
print("EJ8:", "si" if num in list_num else "no")

# EJ9.1 
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
ordenada = []
copia = list_num[:]
while copia:
    m = min(copia)
    ordenada.append(m)
    copia.remove(m)
print("EJ9.1:", ordenada)

# EJ9.2 
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
for i in range(len(list_num)):
    mi = i
    for j in range(i+1, len(list_num)):
        if list_num[j] < list_num[mi]:
            mi = j
    list_num[i], list_num[mi] = list_num[mi], list_num[i]
print("EJ9.2:", list_num)

# EJ9.3 
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
for i in range(1, len(list_num)):
    k = list_num[i]
    j = i - 1
    while j >= 0 and list_num[j] > k:
        list_num[j+1] = list_num[j]
        j -= 1
    list_num[j+1] = k
print("EJ9.3:", list_num)
