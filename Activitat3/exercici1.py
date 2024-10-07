numero = int(input("Introdueix un número entre 10 i 100: "))

if numero < 10 or numero > 100:
    print("El número ha de ser entre 10 i 100.")
else:
    numeros_tupla = tuple(i for i in range(1, numero + 1))
    print(f"Els números de l'1 fins al {numero} són: {numeros_tupla}")
