import os

class Passagerare:
    def __init__(self, alder, kon):
        self.alder = alder
        self.kon = kon
    
    def reagera(self):
        if self.alder < 12:
            return "Passageraren (barn) ler och viftar"
        elif self.alder < 20:
            return "Passageraren (tonåring) rullar med ögonen"
        elif self.kon == "man":
            return "Passageraren (man) nickar artigt"
        else:
            return "Passageraren (kvinna) ler försiktigt"

class Buss:
    def __init__(self):
        self.passagerare = []
        self.antal_passagerare = 0
        self.MAX_PASSAGERARE = 25

    def run(self):
        print("Välkommen till Buss-simulatorn")
        while True:
            val = input("1) Lägg till passagerare\n2) Skriv ut passagerare\n3) Total ålder\n4) Genomsnittsålder\n5) Högsta ålder\n6) Åldersintervall\n7) Sortera efter ålder\n8) Avsluta\n9) Rensa skärmen\nVal: ")
            if val == "1":
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

    def lagg_till_passagerare(self):
        if self.antal_passagerare < self.MAX_PASSAGERARE:
            alder = int(input("Ange ålder: "))
            kon = input("Ange kön (man/kvinna): ")
            passagerare = Passagerare(alder, kon)
            self.passagerare.append(passagerare)
            self.antal_passagerare += 1
            print("Passageraren lades till.")
        else:
            print("Bussen är full, ingen plats för fler passagerare.")

    def skriv_ut_buss(self):
        if self.antal_passagerare > 0:
            print("Passagerare:")
            for i, p in enumerate(self.passagerare):
                print(f"{i+1}. Ålder: {p.alder}, Kön: {p.kon}")
        else:
            print("Bussen är tom.")

    def rakna_total_alder(self):
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
        
    def rensa_skarm(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

if __name__ == "__main__":
    minbuss = Buss()
    minbuss.run()