# Game of life
# Boy Bouwense s1102301

# een function die een generatie mooi print
def toon_generatie(generatie):
    for x in range(len(generatie)):
        for y in generatie[x]:
            if y:
                print("X", end="")
            else:
                print("O", end="")
        print()
    print()

# een function die voor een coordinaat in de lijst met lijsten het aantal buren berekent
def toon_buren(generatie, y, x):
    buren_counter = 0
    # Allemaal if statements die checken welke buren leven en voegt die toe aan de buren counter
    if x + 1 <= len(generatie[y]) - 1:
        if generatie[y][x + 1]:
            buren_counter += 1
    if x - 1 >= 0:
        if generatie[y][x - 1]:
            buren_counter += 1
    if y + 1 <= len(generatie) - 1:
        if generatie[y + 1][x]:
            buren_counter += 1
    if y - 1 >= 0:
        if generatie[y - 1][x]:
            buren_counter += 1
    if x + 1 <= len(generatie[y]) - 1 and y - 1 >= 0:
        if generatie[y - 1][x + 1]:
            buren_counter += 1
    if x - 1 >= 0 and y - 1 >= 0:
        if generatie[y - 1][x - 1]:
            buren_counter += 1
    if y + 1 <= len(generatie) - 1 and x + 1 <= len(generatie[y]) - 1:
        if generatie[y + 1][x + 1]:
            buren_counter += 1
    if y + 1 <= len(generatie) - 1 and x - 1 >= 0:
        if generatie[y + 1][x - 1]:
            buren_counter += 1
    return buren_counter

# een function die de volgende genereerd
def volgende_generatie(generatie):
    niewe_generatie = []
    # nested foor loops die voor elke cel kijkt hoeveel buren ze hadden in de vorige generatie en bepaalt of ze in de
    # volgende generatie leven of niet
    for y in range(len(generatie)):
        tussen_list = []
        for x in range(len(generatie[y])):
            if not generatie[y][x] and toon_buren(generatie, y, x) == 3:
                tussen_list.append(True)
            elif generatie[y][x] and (toon_buren(generatie, y, x) >= 4 or toon_buren(generatie, y, x) < 2):
                tussen_list.append(False)
            elif generatie[y][x]:
                tussen_list.append(True)
            else:
                tussen_list.append(False)
        niewe_generatie.append(tussen_list)
    return niewe_generatie

# een function die de input omzet in een generatie bestaand uit een lijst in een lijst
def input_parser(generatie_string):
    generatie = []
    temp_list = []
    # een for loop die door alle string elementen heen loopt en er zo een lijst in lijsten van maakt
    for x in generatie_string:
        if x.lower() == "x":
            temp_list.append(True)
        elif x.lower() == "o":
            temp_list.append(False)
        elif x == ",":
            generatie.append(temp_list)
            temp_list = []
    generatie.append(temp_list)
    return generatie

#  de main function
def main():
    # de invoer wordt door de input_parser gegooid
    invoer = input("maak een spelbord door middel van dit formaat XXOO,OOXX,XXOX,XOOX etc.(letter X of letter O)\n"
                   "de comma's geven een nieuwe regel aan (alle regels moeten even lang zin): ")
    generatie = input_parser(invoer)
    toon_generatie(generatie)
    genloop = True
    # een while loop die blijft vragen of de gebruiker een nieuwe generatie wilt zien
    while genloop:
        if input("wilt u de volgende generatie zien te ja of te nee") == "ja":
            generatie = volgende_generatie(generatie)
            toon_generatie(generatie)
        else:
            genloop = False


if __name__ == "__main__":
    main()