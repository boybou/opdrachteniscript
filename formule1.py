# Formule 1
# Boy Bouwense S1102301

grotePrijsLLandnaam = input("voer grand prix land ")
aantalKmPerRonde = float(input("voer afstand van één enkele ronde in(in km): "))
gemiddeldeTijdPerRonde = float(input("voer gemiddelde tijd per één enkele ronde(minuten): "))

teOverschreidenAfstand = 305
maximaleTijd = 120

if teOverschreidenAfstand % aantalKmPerRonde == 0:
    aantalRondes = teOverschreidenAfstand / aantalKmPerRonde
else:
    aantalRondes = (teOverschreidenAfstand // aantalKmPerRonde) + 1

if not(aantalRondes*gemiddeldeTijdPerRonde <= maximaleTijd):
    if maximaleTijd % gemiddeldeTijdPerRonde == 0:
        aantalRondes = maximaleTijd / gemiddeldeTijdPerRonde
    else:
        aantalRondes = (maximaleTijd // gemiddeldeTijdPerRonde)+1
geredenKm = aantalRondes * aantalKmPerRonde
print("De grote prijs van %s wordt verreden over %i ronden (%0.3f km)." %(grotePrijsLLandnaam,aantalRondes,geredenKm) )

