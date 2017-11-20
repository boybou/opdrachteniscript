grotePrijsLLandnaam = input("voer grand prix land ")
afstandPerRonde = float(input("voer afstand van één enkele ronde in: "))
gemiddeldeTijdPerRonde = float(input("voer gemiddelde tijd per één enkele ronde(minuten): "))

teOverschreidenAfstand = 305
maximaleTijd = 120

if teOverschreidenAfstand % afstandPerRonde == 0:
    aantalRondes = teOverschreidenAfstand / afstandPerRonde
else:
    aantalRondes = (teOverschreidenAfstand // afstandPerRonde) + 1

if not(aantalRondes*gemiddeldeTijdPerRonde <= maximaleTijd):
    if maximaleTijd % gemiddeldeTijdPerRonde == 0:
        aantalRondes = maximaleTijd / gemiddeldeTijdPerRonde
    else:
        aantalRondes = (maximaleTijd // gemiddeldeTijdPerRonde)+1
geredenKm = aantalRondes * afstandPerRonde
print("De grote prijs van %s wordt verreden over %i ronden (%0.3f km)." %(grotePrijsLLandnaam,aantalRondes,geredenKm) )

