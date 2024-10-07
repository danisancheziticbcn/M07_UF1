# Inicialitzar diccionari buit
contactes = {}

# Bucle per anar afegint contactes
while True:
    # Demanar nom
    nom = input("Introdueix el nom del contacte (o escriu 'no' per acabar): ").strip()

    # Comprovar si l'usuari vol acabar
    if nom.lower() == 'no':
        break

    # Comprovar si el nom ja està al diccionari
    if nom in contactes:
        print(f"El contacte '{nom}' ja està al diccionari. No s'afegirà.")
    else:
        # Demanar edat
        try:
            edat = int(input(f"Introdueix l'edat de {nom}: "))
            # Afegir nom i edat al diccionari
            contactes[nom] = edat
        except ValueError:
            print("L'edat ha de ser un número vàlid. Torna-ho a intentar.")

# Imprimir els contactes finals
print("\nContactes introduïts:")
for nom, edat in contactes.items():
    print(f"{nom}: {edat} anys")
