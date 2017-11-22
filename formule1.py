# Formule 1
# Boy Bouwense S1102301

# Vraag invoer over de Grand Prix
grotePrijsLLandnaam = input("voer grand prix land ")
aantalKmPerRonde = float(input("voer afstand van één enkele ronde in(in km): "))
gemiddeldeTijdPerRonde = float(input("voer gemiddelde tijd per één enkele ronde(minuten): "))

# Declare 2 constanten
teOverschreidenAfstand = 305
maximaleTijd = 120
# Een if statement die de enige uitzondering van het reglement afhandelt
if grotePrijsLLandnaam == "Monaco" or "monaco":
    aantalRondes = 78
else:
    # Een if statement die checkt of de afstand van de aantal rondes precies over een komt met de te overschreiden afstand
    if teOverschreidenAfstand % aantalKmPerRonde == 0:
        aantalRondes = teOverschreidenAfstand / aantalKmPerRonde
    # Zo niet wordt er een ronde bij opgetelt
    else:
        aantalRondes = (teOverschreidenAfstand // aantalKmPerRonde) + 1
    # Een if statement die checkt of de tijdslimiet wordt overschreden
    if not(aantalRondes*gemiddeldeTijdPerRonde <= maximaleTijd):
        # Een if en else statement die berekenen hoeveel rondes er gereden kunnen worden zonder dat de tijdslimiet wordt
        # overschreden
        if maximaleTijd % gemiddeldeTijdPerRonde == 0:
            aantalRondes = maximaleTijd / gemiddeldeTijdPerRonde
        else:
            aantalRondes = (maximaleTijd // gemiddeldeTijdPerRonde)+1
# De laatste uitvoer variable wordt berekent
geredenKm = aantalRondes * aantalKmPerRonde
# Print uitvoer
print("De grote prijs van %s wordt verreden over %i ronden (%0.3f km)." %(grotePrijsLLandnaam,aantalRondes,geredenKm) )

