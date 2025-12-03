# EJ1
cotxe = {
    "marca": "Toyota",
    "model ": "Corolla",
    "any": 2020
}

print(cotxe["marca"])


# EJ2
el_meu_cotxe = {"marca": "Toyota", "model": "Corolla", "any": 2020}
el_meu_cotxe["color"] = "vermell"
del el_meu_cotxe["any"]
print(el_meu_cotxe)

# EJ3
capitals = {"Espanya": "Madrid", "França": "París", "Itàlia": "Roma"}
for pais, capital in capitals.items():
    print(f"La capital de {pais} és {capital}.")

# EJ4
pais_buscat = input("Digues un país: ")
if pais_buscat in capitals:
    print(f"La capital de {pais_buscat} és {capitals[pais_buscat]}.")
else:
    print(f"No conec la capital d'aquest país, ho sento!")

# EJ5
paraula = input("Escriu una paraula: ")
comptador = {}
for lletra in paraula:
    if lletra in comptador:
        comptador[lletra] += 1
    else:
        comptador[lletra] = 1
print(comptador)
