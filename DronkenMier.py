# Dronken mier
# Boy Bouwense S1102301


def rooster(n, fermonen_spoor_string):
    fermonen_spoor_lijst = []
    fermonen_spoor_inner_lijst = []
    counter = 0
    for x in fermonen_spoor_string:
        fermonen_spoor_inner_lijst.append(x)
        counter += 1
        if counter == n:
            fermonen_spoor_lijst.append(fermonen_spoor_inner_lijst)
            fermonen_spoor_inner_lijst = []
            counter = 0
    return fermonen_spoor_lijst


def tekst(fermonen_spoor_lijst):
    uitvoer_string= ""
    for x in fermonen_spoor_lijst:
        for y in x:
            uitvoer_string += y + " "
        uitvoer_string += "\n"
    return uitvoer_string


def stap(fermonen_spoor_lijst, positie):
    aangepast = False
    while not(aangepast):
        y = positie[0]
        x = positie[1]
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
        if not(y < 0 or y > len(fermonen_spoor_lijst) - 1 or x < 0 or x > len(fermonen_spoor_lijst[positie[0]]) - 1):
            aangepast = True
    positie = (y,x)
    return fermonen_spoor_lijst, positie


def stappen(fermonen_sppor_lijst):



def main():
    vierkant = rooster(4, '>>>>^<^v^v^^>>v>')
    print(vierkant)
    print(tekst(vierkant))
    vierkant, pos =stap(vierkant, (3, 0))
    print(tekst(vierkant))
    vierkant, pos = stap(vierkant, pos)
    print(tekst(vierkant))
    vierkant, pos = stap(vierkant, pos)
    print(tekst(vierkant))
    vierkant, pos = stap(vierkant, pos)
    print(tekst(vierkant))
    vierkant, pos = stap(vierkant, pos)
    print(tekst(vierkant))
    vierkant, pos = stap(vierkant, pos)



if __name__ == "__main__":
    main()
