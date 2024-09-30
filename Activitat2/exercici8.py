
entrada = input("Introdueix entre 1 i 3 paraules separades per espais: ")
paraules = entrada.split()

if len(paraules) < 1 or len(paraules) > 3:
    print("Has d'introduir entre 1 i 3 paraules.")
else:

    for paraula in paraules:
        longitud = len(paraula)
        primer_caracter = paraula[0]
        ultim_caracter = paraula[-1]

        print(f"Paraula: {paraula}")
        print(f"  - Nombre de caràcters: {longitud}")
        print(f"  - Primer caràcter: {primer_caracter}")
        print(f"  - Últim caràcter: {ultim_caracter}")
