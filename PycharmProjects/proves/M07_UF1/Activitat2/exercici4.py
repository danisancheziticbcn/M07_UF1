valor1 = float(input("Introdueix el primer valor: "))
valor2 = float(input("Introdueix el segon valor: "))

opcio = ''
while opcio not in ['1', '2', '3', '4']:
    print("Tria l'operació que vols realitzar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicació")
    print("4. Divisió")
    opcio = input("Escriu el número de l'operació (1-4): ")

    if opcio not in ['1', '2', '3', '4']:
        print("Opció no vàlida. Si us plau, tria un número entre 1 i 4.")

if opcio == '1':
    resultat = valor1 + valor2
    print(f"La suma de {valor1} i {valor2} és: {resultat}")
elif opcio == '2':
    resultat = valor1 - valor2
    print(f"La resta de {valor1} i {valor2} és: {resultat}")
elif opcio == '3':
    resultat = valor1 * valor2
    print(f"La multiplicació de {valor1} i {valor2} és: {resultat}")
elif opcio == '4':
    if valor2 != 0:
        resultat = valor1 / valor2
        print(f"La divisió de {valor1} entre {valor2} és: {resultat}")
    else:
        print("No es pot dividir per zero!")
