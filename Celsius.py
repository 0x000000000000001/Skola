#Metoden för att konvertera Fahrenheit till Celsius
def fahr_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) * 5 // 9
    return celsius

# Tar emot temperatur i Fahrenheit och skriver i konsolen ut Temperaturen i Celsius
user_input = int(input("Ange temperaturen i Fahrenheit: "))
celsius_value = fahr_to_cel(user_input)
print(f"{user_input} Fahrenheit motsvarar {celsius_value} Celsius.")