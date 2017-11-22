# Interessante getallen
# Boy Bouwense S1102301
# HEADS  UP: als deze code getest wordt en er worden hoge getallen ingevult kan het een redelijk lange tijd duren
# voordat de uitkosmt berekend is

# initeer een list zodat er getallen aan toegevoegd kunnen worden
nList = []
# Vraag hoeveel getallen er getest moeten worden
t = int(input("hoeveel getallen wilt u testen?: "))
# Vraag de invoer van alle testgevallen
for x in range(t):
    nList.append(int(input("getal %i: " % (x + 1))))
# een for loop die alle testgevallen doorloopt en het uitkomst getal berekent
for x in nList:
    n = 0
    checkGetalGevonden = False
    # while loop die checkt of de som van alle cijfers van een getal gelijk is aan een x
    # er hoeft niet gecheckt te worden of het getal door x deelbaar is omdat er de hele tijd x bij opgeteld wordt en het
    # dus altijd deelbaar zou zijn door x
    while not checkGetalGevonden:
        iGetalSum = 0
        striGetal = str(n)
        # for loop die alle cijfers van een getal optelt
        for y in range(len(striGetal)):
            iGetalSum += int(striGetal[y])
        if iGetalSum == x:
            # print uitvoor van testgeval
            print("uitkomst van getal %i is: %i" % (x, n))
            checkGetalGevonden = True
        n += x