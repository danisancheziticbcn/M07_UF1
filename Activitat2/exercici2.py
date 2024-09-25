
valor = float(input(f"introdueix un valor en €: "))
iva = int(input(f"introdueix l'iva a aplicar: "))

while iva not in [4,10,21]:
    iva = int(input(f"Iva incorrecte. Introdueix l'iva a aplicar: "))

print(f"El valor introduit inicialment és de: {valor} €")
print(f"L'iva a aplicar és de {iva} %")
nouv = ((iva / 100) * valor) + valor
print(f"El nou valor amb l'iva inclós és de {nouv} €")