# Double Dutch
# Boy Bouwense S1102301


def medeklinkers(bestand_path):
    bestand = open(bestand_path, 'r')
    vertalingen = bestand.read()
    bestand.close()
    vertalingen_dict = {}
    medeklinker_dict = {"b":False,"k":False,"s":False,"c":False,"l":False,"t":False,"d":False,"m":False,"v":False,
                        "f":False,"n":False,"w":False,"g":False,"p":False,"x":False,"h":False,"q":False,"y":False,
                        "j":False,"r":False,"z":False}
    temp_medeklinker = ""
    temp_medeklinker_vert = ""
    medeklinker_gehad = False
    for x in vertalingen:
        if x.isalpha() and not(medeklinker_gehad):
            temp_medeklinker = x
            if x in medeklinker_dict:
                if medeklinker_dict[x]:
                    raise AssertionError("ongeldige vertaling")
                else:
                    medeklinker_dict[x] = True
            else:
                raise AssertionError("ongeldige vertaling")
        elif x == "-":
            medeklinker_gehad = True
        elif x == "\n":
            vertalingen_dict.update({temp_medeklinker: temp_medeklinker_vert})
            medeklinker_gehad = False
            temp_medeklinker = ""
            temp_medeklinker_vert = ""
        elif x.isalpha() and medeklinker_gehad and temp_medeklinker_vert == "" and x != temp_medeklinker:
            raise AssertionError("ongeldige vertaling")
        elif x.isalpha() and medeklinker_gehad:
            temp_medeklinker_vert += x
    true_counter = 0
    for x in medeklinker_dict:
        if medeklinker_dict[x]:
            true_counter += 1
    if true_counter < len(medeklinker_dict):
        raise AssertionError("ongeldige vertaling")

    return vertalingen_dict


def vertaal_woord(woord, dict):
    vertaalde_woord = ""
    last_letter = ""
    for x in woord:
        if x.lower() in dict and last_letter == x:
            vertaalde_woord = vertaalde_woord[:-len(dict[x.lower()])]
            if last_letter.isupper():
                vertaalde_woord += "Sqau" + dict[x.lower()]
            else:
                vertaalde_woord += "sqau" + dict[x.lower()]
            last_letter = ""
        elif x.lower() in dict:
            if x.isupper():
                vertaalde_woord += dict[x.lower()][0].upper()
                vertaalde_woord += dict[x.lower()][1:]
            else:
                vertaalde_woord += dict[x.lower()]
            last_letter = x
        elif x == last_letter:
            vertaalde_woord = vertaalde_woord[:-len(x)]
            if last_letter.isupper():
                vertaalde_woord += "Squat" + x + "h"
            else:
                vertaalde_woord += "squat" + x + "h"
            last_letter = ""
        else:
            vertaalde_woord += x
            last_letter = x
    return vertaalde_woord


def vertaal(zin, dict):
    vertaalde_zin = ""
    temp_woord = ""
    for y, x in enumerate(zin):
        if x.isalpha() and y == (len(zin)-1):
            temp_woord += x
            vertaalde_zin += vertaal_woord(temp_woord, dict)
        elif x.isalpha():
            temp_woord += x
        elif not(x.isalpha()):
            vertaalde_zin += vertaal_woord(temp_woord, dict)
            temp_woord = ""
            vertaalde_zin += x
        else:
            vertaalde_zin += x
    return vertaalde_zin


def main():
    dutchLetter = medeklinkers('dutchLetters.txt')
    print(dutchLetter['s'])
    print(dutchLetter['q'])
    print(dutchLetter['d'])
    print(vertaal_woord('took', dutchLetter))
    print(vertaal_woord('BAMBOO', dutchLetter))
    print(vertaal_woord('Yesterday', dutchLetter))
    print(vertaal('I took a walk to the park yesterday.', dutchLetter))


if __name__ == "__main__":
    main()