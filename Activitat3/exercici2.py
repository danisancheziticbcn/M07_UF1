mesos = ("Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre")

while True:
    numero = int(input("Introdueix un número entre 1 i 12 per veure el mes corresponent (0 per sortir): "))
    if numero == 0:
        print("Programa finalitzat.")
        break
    elif numero < 1 or numero > 12:
        print("El número ha de ser entre 1 i 12. Torna a intentar-ho.")
    else:
        print(f"El mes número {numero} és: {mesos[numero - 1]}")
