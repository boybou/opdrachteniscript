# GSMoniemen
# Boy Bouwense S1102301

# een function die de T9 cijfercombinatie bij een woord zoekt
def t9(woord):
    # declare voor elke toets de bijbehorende letters
    toets2 = ["a","b","c"]
    toets3 = ["d","e","f"]
    toets4 = ["g","h","i"]
    toets5 = ["j","k","l"]
    toets6 = ["m", "n", "o"]
    toets7 = ["p", "q", "r", "s"]
    toets8 = ["t", "u", "v"]
    toets9 = ["w", "x", "y", "z"]
    # stop alle toetsen in een toetsen list
    toetsen = [toets2, toets3, toets4, toets5, toets6, toets7, toets8, toets9]
    # declare een lege string zodat er cijfers aan toegevoegd kunnen worden
    cijfer_combinatie = ''
    # een for loop die alle letters van het woord doorloopt
    for x in woord:
        # een for loop die voor elke toets checkt of de letter er in voor komt zo ja wordt die toegevoegd aan de string
        for y in toetsen:
            if x.lower() in y:
                cijfer_combinatie += str(toetsen.index(y)+2)
    # returned de cijfercombinatie string
    return cijfer_combinatie

# een function die voor 2 woorden checkt of ze de zelfde T9 cijfercombinatie's hebben
def gsmoniemen(woord1, woord2):
    # checkt of de t9 cijfercombienatie van bijde woorden gelijk zijn en returned respectievelijk true of false
    if t9(woord1) == t9(woord2):
        return True
    else:
        return False

# de main function
def main():
    # alle invoer wordt gevraagd
    t9_woord = input("voer een woord in waar u de t9 cijfercombinatie van wilt: ")
    gsmoniem_invoer1 = input("geef een woord waarvan u wilt testen of het een gsmoniem is (woord 1 van de 2): ")
    gsmoniem_invoer2 = input("geef een woord waarvan u wilt testen of het een gsmoniem is (woord 2 van de 2): ")
    # een stukje code om de uitvoer van de gsmoniemen functie goed weer te geven
    gsmoniem_uitvoer = ""
    if not(gsmoniemen(gsmoniem_invoer1,gsmoniem_invoer2)):
        gsmoniem_uitvoer = "geen "
    # print de 2 uitvoer regels
    print("\nde T9 cijfercombinatie van het woord %s is: %s" % (t9_woord, t9(t9_woord)))
    print("de woorden %s en %s zijn %sGSMoniemen" % (gsmoniem_invoer1, gsmoniem_invoer2, gsmoniem_uitvoer))


if __name__ == "__main__":
    main()
