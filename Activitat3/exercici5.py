frase = input("Introdueix una frase: ")
frase_sense_espais = frase.replace(" ", "")
tupla_caracters = tuple(frase_sense_espais)

caracters_unics = []
for caracter in frase_sense_espais:
    if caracter not in caracters_unics:
        caracters_unics.append(caracter)

frase_sense_repetits = ''.join(caracters_unics)

print(f"Contingut de la tupla: {tupla_caracters}")
print(f"Frase sense caràcters repetits: {frase_sense_repetits}")


