# LevensVerwachting
# Boy Bouwense S1102301

# een function die de levensverwachting van een persoon bepaald aan de hand van een paar factoren
def levensverwachting(geslacht, roker, sport, alcohol, fastfood):
    # declare standaard verwachte leeftijd
    verwachteLeeftijd = 70.0
    # if statement die checkt of het geslacht een vrouw is en telt er de benodigde jaren bij op
    if geslacht == "vrouw":
        verwachteLeeftijd += 4
    # if statement die checkt of de persoon rookt en trekt er de benodigde jaren af
    if roker:
        verwachteLeeftijd -= 5
    else:
        verwachteLeeftijd += 5
    # if statement die checkt hoeveel uur er per week gesport wordt en telt er de benodigde jaren bij op of af
    if sport == 0:
        verwachteLeeftijd -= 3
    else:
        verwachteLeeftijd += sport
    # if statement die checkt hoeveel glazen alcohol er per week worden geconsumeerd
    # en voert weer de bijbehordende berekening er bij uit
    if alcohol == 0:
        verwachteLeeftijd += 2
    elif alcohol > 7:
        verwachteLeeftijd -= ((alcohol-7)*0.5)
    # if statement die checkt of er veel fastfood wordt gegeten en telt er zo nodig een paar jaar bij op
    if not(fastfood):
        verwachteLeeftijd += 3
    # returned verwachte leeftijd
    return verwachteLeeftijd


# de main function
def main():
    # vraag alle invoer
    geslacht = input("bent u een man of een vrouw: ")
    roker =  input("rookt u te ja of te nee: ")
    sport = int(input("hoeveel uur per week sport u: "))
    alcohol = int(input("hoeveel glazen alcohol drinkt u per week: "))
    fastfood = input("eet u vaak fast food te ja of te nee: ")
    fastfoodbool = False
    rokerbool = False
    # 2 if statements die ervoor zorgen dat de roker en fastfood invoer een boolean vorm krijgt
    if fastfood == "ja":
        fastfoodbool = True
    if roker == "ja":
        rokerbool = True
    # print de uitvoer
    print("u levensverwachting is %3.1f" % levensverwachting(geslacht, rokerbool, sport, alcohol, fastfoodbool))


if __name__ == "__main__":
    main()