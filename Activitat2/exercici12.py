numero = int(input("Introdueix un número: "))
suma = 0

for i in range(1, numero + 1):
    suma += i

print(f"La suma de tots els números des de l'1 fins al {numero} és: {suma}")
