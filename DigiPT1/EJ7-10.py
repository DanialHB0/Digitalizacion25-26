#EJ7
paraula = "programacio"
nombre_de_lletres = len(paraula)

print("La paraula", paraula)
print("Te", nombre_de_lletres, "lletres")

#EJ8
nombre = (0, 1, 2, 3, 4, 5, 6, 7, 8)
print("Lista de numeros desde el 0 al 8")
for i in nombre:
	print(i)
	
#EJ9
nombre1 = 15
nombre2 = 9
nombre3 = 12

maximo = nombre1  
if nombre2 > maximo:
    maximo = nombre2

if nombre3 > maximo:
    maximo = nombre3

print("El nombre més gran és:", maximo)

#EJ10
frase = "Hola, mundo!"
frase_invertida = frase[::-1]

print("Frase original:", frase)
print("Frase invertida:", frase_invertida)

