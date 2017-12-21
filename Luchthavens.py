# Luchthavens
# Boy Bouwense s1102301
import math


def lees_luchthavens(bestands_path):
    bestand = open(bestands_path,"r")
    bestand_inhoud = bestand.read()
    bestand.close()
    luchthaven_dict = {}
    column_namen_geweest = False
    temp_code = ""
    temp_longitude = ""
    temp_latitude = ""
    temp_city = ""
    temp_state = ""
    counter = 0
    for y,x in enumerate(bestand_inhoud):
        if column_namen_geweest:
            if counter == 0 and x != "\t" and x != "\n" and (x.isalpha() or x.isdigit()):
                temp_code += x
            elif counter == 1 and x != "\t" and x != "\n":
                temp_latitude += x
            elif counter == 2 and x != "\t" and x != "\n":
                temp_longitude += x
            elif counter == 3 and x != "\t" and x != "\n":
                temp_city += x
            elif counter == 4 and x != "\t" and x != "\n":
                temp_state += x
            if y == len(bestand_inhoud)-1:
                luchthaven_dict.update(
                    {temp_code: (float(temp_latitude), float(temp_longitude), temp_city, temp_state)})
                counter = 0
                temp_code = ""
                temp_longitude = ""
                temp_latitude = ""
                temp_city = ""
                temp_state = ""
            if x == "\t":
                counter += 1
            elif x == "\n":
                luchthaven_dict.update(
                    {temp_code: (float(temp_latitude), float(temp_longitude), temp_city, temp_state)})
                counter = 0
                temp_code = ""
                temp_longitude = ""
                temp_latitude = ""
                temp_city = ""
                temp_state = ""

        if not (column_namen_geweest) and x == "\n":
            column_namen_geweest = True
    return luchthaven_dict


def afstand(code1, code2, dict):
    l1 = math.radians(dict[code1][1])
    b1 = math.radians(dict[code1][0])
    l2 = math.radians(dict[code2][1])
    b2 = math.radians(dict[code2][0])
    afstand = 6372.795 * math.atan((math.sqrt((math.cos(b2)*math.sin(l1-l2))**2+(math.cos(b1)*math.sin(b2)-math.sin(b1)*math.cos(b2)*math.cos(l1-l2))**2))/(math.sin(b1)*math.sin(b2)+math.cos(b1)*math.cos(b2)*math.cos(l1-l2)))
    return afstand


def tussenlanding(code1, code2, luchthavens, reikwijdte = 4000):
    if afstand(code1,code2, luchthavens) <= reikwijdte:
        return None
    else:
        beste_waarde1 = reikwijdte+1
        beste_waarde2 = reikwijdte+1
        totaal_afstand1 = (reikwijdte+1)*2
        best_totaal = (reikwijdte+1)*2
        return_code = ""
        for x in luchthavens:
            if afstand(code1,x, luchthavens) <= reikwijdte and afstand(code2,x, luchthavens) <= reikwijdte and (x != code1 or x != code2):
                beste_waarde1 = afstand(code1,x, luchthavens)
                beste_waarde2 = afstand(code2, x, luchthavens)
            totaal_afstand1 = beste_waarde2 + beste_waarde1
            if totaal_afstand1 < best_totaal:
                return_code = x
                best_totaal = beste_waarde2 + beste_waarde1
        if beste_waarde1 == reikwijdte+1 or beste_waarde2 == reikwijdte+1:
            return None
        return return_code


def main():
    luchthavens = lees_luchthavens("luchthavens.txt")
    print(luchthavens)
    print(luchthavens['ADK'])
    print(luchthavens['DCA'])
    print(luchthavens['4OM'])
    print(afstand('P60', 'MSN', luchthavens))
    print(afstand('ADK', 'DCA', luchthavens))
    print(tussenlanding('ADK', 'DCA', luchthavens, 4000))


if __name__ == "__main__":
    main()