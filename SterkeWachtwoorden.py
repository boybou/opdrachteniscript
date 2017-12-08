# SterkeWachtwoorden
# Boy Bouwense S1102301


# een function die de sterkte van een wachtwoord bepaalt
def bepaal_wachtwoord_sterkte(wachtwoord):
    # een dictionary waar alle sterkheids factoren in staan
    sterk = { "lengte" : False, "hoofdletter" : False, "kleineletter" : False, "cijfer" : False, "speciaalkarakter" : False}
    # een if statement die de lengte van het wachtwoord beoordeeldt
    if len(wachtwoord) >= 8:
        sterk["lengte"] = True
    # een for loop die alle tekens van het wachtwoord doorloopt
    for x in wachtwoord:
        # if statement die checkt of het een hoofdletter is
        if x.isupper():
            sterk["hoofdletter"] = True
        # if statement die checkt of het een kleine letter is
        if x.islower():
            sterk["kleineletter"] = True
        # if statement die checkt of het een cijfer is
        if x.isdigit():
            sterk["cijfer"] = True
        # if statement die checkt of het een speciaal teken is
        if not(x.isdigit() or x.isalpha()):
            sterk["speciaalkarakter"] = True
    sterk_counter = 0
    # een for loop die alle sterkheids factoren die true zijn optelt
    for x in sterk:
        if sterk[x]:
            sterk_counter +=1
    # een if statement die voor het aantal sterken factoren de sterkte bepaalt
    if sterk_counter == 5:
        return "sterk"
    elif sterk_counter == 3 or sterk_counter == 4:
        return "matig"
    else:
        return "zwak"

# de main function
def main():
    # een lege list waar wachtwoorden aan toegevoegd kunnen worden
    ww_list = []
    # vraag hoeveel wachtwoorden er getest moeten worden
    t = int(input("aantal wachtwoorden dat gestest moet worden: "))
    # een for loop die voor hoeveel wachtwoorden er getest moeten worden wachtwoorden als invoer vraagt
    for x in range(t):
        ww_list.append(input("wachtwoord %i: " % (x+1)))
    # print de uitvoer
    print()
    counter = 1
    # for loop die alle wachtwoorden doorloopt en hun sterkte checkt en de uitvoer print
    for x in ww_list:
        print("wachtwoord %i is een %s wachtwoord" % (counter, bepaal_wachtwoord_sterkte(x)))
        counter += 1


if __name__ == "__main__":
    main()

