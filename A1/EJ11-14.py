#EJ11

#EJ12

#EJ13
text = "Hello World"

text_minusculas = text.lower()
text_mayusculas = text.upper()

print("Original:", text)
print("Minusculas:", text_minusculas)
print("Mayusculas:", text_mayusculas)

#EJ14
text = "hola"
text_invertit = ""

for i in range(len(text) - 1, -1, -1):
    text_invertit += text[i]

print("Original:", text)
print("Invertida:", text_invertit)