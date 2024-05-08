using System;

using System;

class GissaTalet
{
    static void Main()
    {
        Random rnd = new Random();
        // Slumpar fram ett hemligt tal mellan 1 och 100
        int hemligtTal = rnd.Next(1, 101);

        int gissning = 0;

        while (gissning != hemligtTal)
        {
            // Tar emot en gissning från användaren
            Console.Write("Gissa talet mellan 1 och 100: ");
            gissning = Convert.ToInt32(Console.ReadLine());

            if (gissning < 1 || gissning > 100)
            {
                Console.WriteLine("Du måste skriva in ett tal mellan 1 och 100!");
            }
            else if (gissning < hemligtTal)
            {
                Console.WriteLine("Ditt tal är för litet. Gissa på ett större tal.");
            }
            else if (gissning > hemligtTal)
            {
                Console.WriteLine("Ditt tal är för stort. Gissa på ett mindre tal.");
            }
            else
            {
                Console.WriteLine("Grattis! Du gissade rätt tal!");
            }
        }
        
        Console.WriteLine("Programmet är slut");
    }
}3