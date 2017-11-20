# Interessante getallen
# Boy Bouwense S1102301

nList = []
t = int(input("hoeveel getallen wilt u testen?: "))
for x in range(t):
    invoer = int(input("getal %i: " % (x + 1)))
for x in nList:
    iGetal = 0
    checkGetalGevonden = False
    while not checkGetalGevonden:
        if iGetal % x == 0:
            iGetalSum = 0
            striGetal = str(iGetal)
            for y in range(len(striGetal)):
                iGetalSum += int(striGetal[y])
            if iGetalSum == x:
                print("uitkomst van getal %i is: %i"%(x,iGetal))
                checkGetalGevonden = True
        iGetal += 1
