numero = int(input("Introdueix un número entre 1 i 10: "))

if numero < 1 or numero > 10:
    print("El número ha de ser entre 1 i 10.")
else:
    taula_multiplicar = tuple(numero * i for i in range(1, 11))
    resultat = ', '.join(f"{valor}" for valor in taula_multiplicar)
    print(f"La taula de multiplicar de {numero} és: {resultat}")