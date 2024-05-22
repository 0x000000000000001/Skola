import os #Används för att vi senare skede ska kunna rensa terminalen.

class Passagerare: #Klassdefinition
    def __init__(self, alder, kon): #Metod som kallas konstruktor - Metoden __init__ används för att initialisera objektets attributer
        self.alder = alder #Self.alder och Self.kon är attribut som tillhör klassen.
        self.kon = kon
    
    def reagera(self): #Metod definition (Detta definierar en metod som heter 'reagera' inom Klassen Passagerare)
        if self.alder < 12:
            return "Passageraren (barn) ler och viftar"
        elif self.alder < 20:
            return "Passageraren (tonåring) rullar med ögonen"
        elif self.kon == "man":
            return "Passageraren (man) nickar artigt"
        else:
            return "Passageraren (kvinna) ler försiktigt"

class Buss: #Klass definition
    def __init__(self):
        self.passagerare = []
        self.antal_passagerare = 0
        self.MAX_PASSAGERARE = 25

    def run(self): #Metod definition (Metoden definierar en funktion som heter 'run' inom klassen 'Buss')
        print("Välkommen till Buss-simulatorn")
        while True: #Skapar en oändlig loop för menyn
            val = input("1) Lägg till passagerare\n2) Skriv ut passagerare\n3) Total ålder\n4) Genomsnittsålder\n5) Högsta ålder\n6) Åldersintervall\n7) Sortera efter ålder\n8) Avsluta\n9) Rensa skärmen\nVal: ")
            if val == "1": #Om användaren skulle välja '1' så anropas metoden 'lagg_till_passagerare' för att lägga till en ny passagerare
                self.lagg_till_passagerare()
            elif val == "2":
                self.skriv_ut_buss()
            elif val == "3":
                print(f"Total ålder: {self.rakna_total_alder()}")
            elif val == "4":
                print(f"Genomsnittsålder: {self.rakna_genomsnittsalder():.2f}")
            elif val == "5":
                print(f"Högsta ålder: {self.hitta_hogsta_alder()}")
            elif val == "6":
                min_alder = int(input("Ange lägsta ålder: "))
                max_alder = int(input("Ange högsta ålder: "))
                positioner = self.hitta_aldersintervall(min_alder, max_alder)
                print(f"Positioner för åldersintervall {min_alder}-{max_alder}: {positioner}")
            elif val == "7":
                self.sortera_buss()
            elif val == "8":
                break
            elif val == "9":
                self.rensa_skarm()
            else:
                print("Ogiltigt val, försök igen.")

    def lagg_till_passagerare(self): #Metod defintion (Skapar en metod som heter 'lagg_till_passagerare' inom klassen 'Buss' )
        if self.antal_passagerare < self.MAX_PASSAGERARE: #Koden kontrollerar om det finns plats för fler passagerare i bussen genom att jämföra det aktuella antalet passagerare (self.antal_passagerare) med det maximala antalet passagerare som bussen kan rymma (self.MAX_PASSAGERARE).
            alder = int(input("Ange ålder: "))
            kon = input("Ange kön (man/kvinna): ")
            passagerare = Passagerare(alder, kon)
            self.passagerare.append(passagerare)
            self.antal_passagerare += 1
            print("Passageraren lades till.")
        else:
            print("Bussen är full, ingen plats för fler passagerare.")

    def skriv_ut_buss(self):
        if self.antal_passagerare > 0: #Kontrollerar om det finns passagerare i bussen
            print("Passagerare:") ## Skriver ut en rubrik för passagerarna
            for i, p in enumerate(self.passagerare): ## Loopar igenom varje passagerare och skriver ut deras ålder och kön
                print(f"{i+1}. Ålder: {p.alder}, Kön: {p.kon}")
        else:
            print("Bussen är tom.")

    def rakna_total_alder(self): #Summerar åldrarna för alla passagerare i bussen
        total_alder = sum(p.alder for p in self.passagerare)
        return total_alder

    def rakna_genomsnittsalder(self):
        if self.antal_passagerare > 0:
            total_alder = self.rakna_total_alder()
            genomsnittsalder = total_alder / self.antal_passagerare
            return genomsnittsalder
        else:
            return 0

    def hitta_hogsta_alder(self):
        if self.antal_passagerare > 0:
            hogsta_alder = max(p.alder for p in self.passagerare)
            return hogsta_alder
        else:
            return 0

    def hitta_aldersintervall(self, min_alder, max_alder):
        positioner = []
        for i, p in enumerate(self.passagerare):
            if min_alder <= p.alder <= max_alder:
                positioner.append(i+1)
        return positioner

    def sortera_buss(self):
        self.passagerare.sort(key=lambda p: p.alder)
        print("Bussen sorterad efter ålder.")
        
    def rensa_skarm(self): #Rensar terminalskärmen, använder olika kommandon beroende på operativsystem
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

if __name__ == "__main__":
    minbuss = Buss() #Skapar en instans av Buss-klassen
    minbuss.run() #Startar bussens körning