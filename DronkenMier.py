# Dronken mier
# Boy Bouwense S1102301


# een function die van een string een lijst in een lijst maakt en zo het rooster returned
def rooster(n, fermonen_spoor_string):
    # if statement die checkt of de ingevoerde string wel lang genoeg is, zo niet wordt er een exception geraised
    if n ** 2 != (len(fermonen_spoor_string)):
        raise AssertionError("ongeldige argumenten")
    fermonen_spoor_lijst = []
    fermonen_spoor_inner_lijst = []
    counter = 0
    # for loop die van de string een een lijst in een lijst maakt
    for x in fermonen_spoor_string:
        fermonen_spoor_inner_lijst.append(x)
        counter += 1
        if counter == n:
            fermonen_spoor_lijst.append(fermonen_spoor_inner_lijst)
            fermonen_spoor_inner_lijst = []
            counter = 0
    return fermonen_spoor_lijst


# een function die van een lijst in een lijst een mooi rooster genereerd
def tekst(fermonen_spoor_lijst):
    uitvoer_string= ""
    # nested for loop die een mooie rooster string genereerd
    for x in fermonen_spoor_lijst:
        for y in x:
            uitvoer_string += y + " "
        uitvoer_string += "\n"
    return uitvoer_string


# een function die een stap van de mier simuleert
def stap(fermonen_spoor_lijst, positie):
        y = positie[0]
        x = positie[1]
        # een aantal if statements die checken welke kant de mier op moet
        if fermonen_spoor_lijst[y][x] == 'v':
            y += 1
            fermonen_spoor_lijst[positie[0]][positie[1]] = '<'
        elif fermonen_spoor_lijst[y][x] == '^':
            y -= 1
            fermonen_spoor_lijst[positie[0]][positie[1]] = '>'
        elif fermonen_spoor_lijst[y][x] == '<':
            x -= 1
            fermonen_spoor_lijst[positie[0]][positie[1]] = '^'
        elif fermonen_spoor_lijst[y][x] == '>':
            x += 1
            fermonen_spoor_lijst[positie[0]][positie[1]] = 'v'
        # een if statement die checkt of de mier niet buiten het rooster loopt en als hij dat wel doet
        # zijn positiet niet veranderd
        if y < 0 or y > len(fermonen_spoor_lijst) - 1 or x < 0 or x > len(fermonen_spoor_lijst[positie[0]]) - 1:
            y = positie[0]
            x = positie[1]
            positie = (y, x)
            return positie
        positie = (y,x)
        return positie


# een fucntion die allemaal stappen simuleert tot dat de rechterbovenhoek van het rooster is bereikt
# beginend in de linkeronderhoek
def stappen(fermonen_spoor_lijst):
    return_lijst = []
    pos = (len(fermonen_spoor_lijst) - 1, 0)
    return_lijst.append(pos)
    # while loop die blijft lopen zolang de mier niet de rechterbovenhoek heeft bereikt
    while pos != (0, len(fermonen_spoor_lijst) - 1):
        pos = stap(fermonen_spoor_lijst, pos)
        return_lijst.append(pos)
    return return_lijst


# de main function
def main():
    # input wordt gevraagd en omgezet naar een rooster
    n = int(input("hoe lang en hoe breed wordt u rooster(1 natuurlijk getal): "))
    inhoud = n ** 2
    fermonen_spoor_string = input("voer u rooster in, u rooster bestaat uit %i tekens(de tekens die u mag gebruiken zijn <,>,v of ^): "
                   % inhoud)
    vierkant = rooster(n, fermonen_spoor_string)
    testvierkant = rooster(n, fermonen_spoor_string)
    voledige_simulatie = stappen(testvierkant)
    # for loopje die de voledige simulatie print
    for x in voledige_simulatie:
        print(tekst(vierkant), "\n")
        stap(vierkant, x)
    print(voledige_simulatie)


if __name__ == "__main__":
    main()
