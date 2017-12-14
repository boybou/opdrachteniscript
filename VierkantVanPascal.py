# Vierkant van pascal
# Boy Bouwense S1102301

# een function die een lijst met lijsten maakt
def vierkant(m, n=1):
    # define alvast de lijsten
    lijst = []
    inner_lijst = []
    # een for loop die de eerste rij vult met n
    for b in range(m):
        inner_lijst.append(n)
    lijst.append(inner_lijst)
    y = 1
    # een nested for loop die voor de eerste kolom ook n invult en de andere kolomen berekent
    for b in range(m-1):
        inner_lijst = []
        inner_lijst.append(n)
        x = 1
        for z in range(m - 1):
            inner_lijst.append(inner_lijst[x-1]+lijst[y-1][x])
            x +=1
        lijst.append(inner_lijst)
        y += 1
    # return de lijst met lijsten
    return lijst

# een function die de vierkant functie gebruikt om van die lijst van lijsten een mooi geformatteerde string te maken
def paden(m, n=1):
    string = ""
    # roept de vierkant fucntie aan
    vierkant_lijst = vierkant(m, n)
    p = len(str(vierkant_lijst[m-1][m-1]))+1
    # nested for loops die de een mooie string maken
    for b in vierkant_lijst:
        for z in b:
            for c in range(p-len(str(z))):
                string +=" "
            string += str(z)
        string += "\n"
    # return de string
    return string



# de main funcite
def main():
    # vraag de invoer
    m = int(input("Voer een natuurlijk getal in dat de lengte en breedte van u vierkant vertegenwoordigd: "))
    n = input("Voer een natuurlijk getal in dat bij de eerste rij en eerste kolom ingevuld wordt(als u niks invult wordt dit 1): ")
    # een if statement die een lege n afvangt
    if n.isdigit():
        n = int(n)
        print("\n",vierkant(m,n),"\n")
        print(paden(m,n))
    else:
        print("\n",vierkant(m),"\n")
        print(paden(m))



if __name__ == "__main__":
    main()