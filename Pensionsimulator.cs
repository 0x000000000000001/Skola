using System;

class PensionSimulator
{
    static void Main(string[] args)
    {
        Console.WriteLine("Välkommen till denna pensionssimulator");
        Console.Write("Vad heter du i förnamn? ");
        string namn = Console.ReadLine();
        Console.Write("Hur gammal är du? ");
        int alder = Convert.ToInt32(Console.ReadLine());
        int arTillPension = 65 - alder;
        Console.WriteLine($"Hej {namn}. Du går i pension om {arTillPension} år.");
        Console.Write("Tryck på en tangent för att avsluta...");
        Console.ReadKey();
    }
}