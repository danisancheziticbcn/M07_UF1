# Demanar a l'usuari que introdueixi 10 números separats per espais
numeros_usuari = input("Introdueix 10 números separats per espais: ")

# Convertir l'entrada a una llista de números enters
llista_numeros = [int(num) for num in numeros_usuari.split()]

# Comprovar que l'usuari ha introduït exactament 10 números
if len(llista_numeros) != 10:
    print("Has d'introduir exactament 10 números.")
else:
    # Calcular la suma total
    suma_total = sum(llista_numeros)

    # Calcular la mitjana
    mitjana = suma_total / len(llista_numeros)

    # Afegir la suma i la mitjana a la llista
    llista_numeros.append(suma_total)
    llista_numeros.append(mitjana)

    # Mostrar per pantalla
    print("\nNúmeros de l'usuari:")
    print(llista_numeros[:-2])  # Mostrem només els 10 números originals
    print(f"Suma total: {suma_total}")
    print(f"Mitjana: {mitjana}")

    # Mostrar la llista completa amb la suma i la mitjana
    print("\nLlista amb suma i mitjana:")
    print(llista_numeros)
