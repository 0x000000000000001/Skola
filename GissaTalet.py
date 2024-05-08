import random

#Slumpar fram ett hemligt tal mellan 1 och 100
hemligtTal = random.randint(1, 100)

gissning = 0

while gissning != hemligtTal:
    #Tar emot en gissning av användaren
    gissning = int(input("Gissa talet mellan 1 och 100: "))

    if gissning < 1 or gissning > 100:
        print("Du måste skriva in ett tal mellan 1 och 100!")
    elif gissning < hemligtTal:
        print("Ditt tal är för litet. Gissa på ett större tal.")
    elif gissning > hemligtTal:
        print("Ditt tal är för stort. Gissa på ett mindre tal.")
    else:
        print("Grattis! Du gissade rätt tal!")


print("Programmet är slut! :)")