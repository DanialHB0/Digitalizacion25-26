a=input("Dona'm un número: ")
b=input("Dona'm un número: ")
c=input("Dona'm un numero")
print("Tipus de dada:", type(a))
if (a.isnumeric() and b.isnumeric()):
    print("Dins el IF")

    print("Sumade ", a, "i", b, "es " ,c)
else:
    print("Dins el ELSE")
    print("No és un número")

print("FINAL")

print("Programa que diu si un número es parell o senar")
n = input("Introdueix un número sencer")
if(n.isnumeric()):
    print("n es numeric")
    reste = a % 2
    if reste == 0:
        print(b, "es parell")
    else: # if reste == 1:
        print(c, "es senar")

else:
    print("Error: Has de introduir un número sencer")
