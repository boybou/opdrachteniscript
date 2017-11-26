alfabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
           "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24,
           "y": 25, "z": 26}


def ontsleutel(rotatie, zin):
    ontsleuteldeZin = ""
    for x in zin:
        if x.lower() in alfabet:
            verkleinderotatie = rotatie % alfabet["z"]
            ontsleuteldeLetterWaarde = alfabet[x.lower()] - verkleinderotatie
            while ontsleuteldeLetterWaarde < alfabet["a"]:
                ontsleuteldeLetterWaarde += alfabet["z"]
            ontsleuteldeLetter = ""
            for z in alfabet:
                if alfabet[z] == ontsleuteldeLetterWaarde:
                    ontsleuteldeLetter = z
            if x == x.lower():
                ontsleuteldeZin += ontsleuteldeLetter
            else:
                ontsleuteldeZin += ontsleuteldeLetter.upper()
        else:
            ontsleuteldeZin += x
    return ontsleuteldeZin


print(ontsleutel(int(input("")), input("")))
