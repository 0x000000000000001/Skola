def fahr_to_cels(fahrenheit):
    celsius = (fahrenheit - 32) * 5 // 9
    return celsius

def main():
    
    celsius = 0

    while celsius < 82 or celsius > 87:
        try:
            fahrenheit = float(input("Ange temperaturen i Fahrenheit: "))
            celsius = fahr_to_cels(fahrenheit)

            if celsius < 82:
                print("Det är för kallt.")
            elif celsius > 87:
                print("Det är för varmt.")
            else:
                print("Temperaturen är nu lagom. Bastun är redo att bada i!")
        except ValueError:
            print("Felaktigt värde. Ange ett numeriskt värde för Fahrenheit.")

if __name__ == "__main__":
    main()