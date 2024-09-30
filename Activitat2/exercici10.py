import random

numero_secret = random.randint(1, 100)

intents = 0

while True:
    intent = int(input("Introdueix un número entre 1 i 100: "))

    intents += 1

    if intent < numero_secret:
        print("El número és més gran!")
    elif intent > numero_secret:
        print("El número és més petit!")
    else:
        print(f"Has encertat! El número era {numero_secret}.")
        print(f"Has necessitat {intents} intents.")
        break
