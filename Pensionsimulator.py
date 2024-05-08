def pension_simulator():
    print("Välkommen till denna pensionssimulator")
    namn = input("Vad heter du i förnamn? ")
    alder = int(input("Hur gammal är du? "))
    ar_till_pension = 65 - alder
    print(f"Hej {namn}. Du går i pension om {ar_till_pension} år.")
    input("Tryck på en tangent för att avsluta...")

pension_simulator()