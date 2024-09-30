
entrada = input("Introdueix dues paraules separades per espai: ")
paraules = entrada.split()

if len(paraules) != 2:
    print("Has d'introduir exactament dues paraules.")
else:
    primera_paraula = paraules[0]
    segona_paraula = paraules[1]

    nova_primera = segona_paraula[:2] + primera_paraula[2:]
    nova_segona = primera_paraula[:2] + segona_paraula[2:]

    print(f"Resultat: {nova_primera} {nova_segona}")
