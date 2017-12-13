# Vierkant van pascal
# Boy Bouwense S1102301


def vierkant(m, n=1):
    lijst = []
    inner_lijst = []

    for b in range(m):
        inner_lijst.append(n)
    lijst.append(inner_lijst)
    y = 1
    for b in range(m-1):
        inner_lijst = []
        inner_lijst.append(n)
        x = 1
        for z in range(m - 1):
            inner_lijst.append(inner_lijst[x-1]+lijst[y-1][x])
            x +=1
        lijst.append(inner_lijst)
        y += 1
    return lijst


def paden(m, n=1):
    string = ""
    vierkant_lijst = vierkant(m, n)
    p = len(str(vierkant_lijst[m-1][m-1]))+1
    for b in vierkant_lijst:
        for z in b:
            for c in range(p-len(str(z))):
                string +=" "
            string += str(z)
        string += "\n"
    return string




def main():

    print(vierkant(3))
    print(vierkant(3, 100))
    print(vierkant(4))
    print(paden(3))
    print(paden(3, 100))
    print(paden(4))
    print(paden(6))
    print(paden(8))
    print(paden(10))



if __name__ == "__main__":
    main()