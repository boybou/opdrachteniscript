# Ceasarrotatie
# Boy Bouwense S1102301


# een function die een zin met een bepaalde ceasarrotatie ontcijfert
def ontsleutel(rotatie, zin):
    # declare een dicitonary om waardes te geven aan elk letter in het alfabet
    alfabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
               "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23,
               "x": 24,
               "y": 25, "z": 26}
    ontsleutelde_zin = ""
    # een for loop die door alle tekens van een zin heen loopt
    for x in zin:
        # een if statement die checkt of het teken een teken is uit het alfabet
        if x.lower() in alfabet:
            # een stukje code die de ceasarrotatie terugdraait
            verkleinderotatie = rotatie % alfabet["z"]
            ontsleutelde_letter_waarde = alfabet[x.lower()] - verkleinderotatie
            while ontsleutelde_letter_waarde < alfabet["a"]:
                ontsleutelde_letter_waarde += alfabet["z"]
            ontsleutelde_letter = ""
            # een for loop die voor een bepaalde letterwaarde het bijbehorende letter in het alfabet zoekt
            for z in alfabet:
                if alfabet[z] == ontsleutelde_letter_waarde:
                    ontsleutelde_letter = z
            # een if statement die checkt of de oorspronkelijke letter een hoofdletter was en respectievelijk de letter
            # in hoofdletter of kleineletter vorm aan de onsleutelde zin toevoegt
            if x == x.lower():
                ontsleutelde_zin += ontsleutelde_letter
            else:
                ontsleutelde_zin += ontsleutelde_letter.upper()
        # zo niet hoeft er niks veranderd te worden en wordt het teken toegevoegd aan de onstleutelde zin
        else:
            ontsleutelde_zin += x
    # returned de onsleutelde zin
    return ontsleutelde_zin

# de main function
def main():
    # invoer wordt gevraagd en gelijk door de ontsleutel functie gehaald
    onsleutelde_zin = ontsleutel(int(input("met hoeveel Caesar rotaties is het bericht versleutelt: ")),
                     input("de versleutelde zin: "))
    # uitvoer wordt geprint
    print("\nontsleutelde zin: %s" % onsleutelde_zin)


if __name__ == "__main__":
    main()
