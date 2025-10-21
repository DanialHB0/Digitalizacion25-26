print("Introdueix un numero en graus celsius")
c = float(input())
f = (c * 9 / 5) + 32
print("Els graus en fahrenheit són:", f)

print("Calcula l'area d'un rectangle")
altura = 4 
amplada = 5
area = altura * amplada
print("L'area del rectangle és:", area)

nombre = 6
print(f"Taula de multiplicar del {nombre}:")
for i in range(1, 11):
    resultat = nombre * i
    print(f"{nombre} x {i} = {resultat}")
