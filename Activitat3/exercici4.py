numeros_input = input("Introdueix 10 números separats per un espai: ")
numeros = list(map(int, numeros_input.split()))

if len(numeros) != 10:
    print("Has d'introduir exactament 10 números.")
else:
    numeros_ordenats = sorted(numeros)
    tupla_numeros = tuple(numeros_ordenats)
    print(f"Els números ordenats són: {tupla_numeros}")
