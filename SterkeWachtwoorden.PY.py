def bepaalwachtwoordSterkte(wachtwoord):
    sterk = { "lengte" : False, "hoofdletter" : False, "kleineletter" : False, "cijfer" : False, "speciaalkarakter" : False}
    if len(wachtwoord) >= 8:
        sterk["lengte"] = True
    for x in wachtwoord:
        if x.isupper():
            sterk["hoofdletter"] = True
        if x.islower():
            sterk["kleineletter"] = True
        if x.isdigit():
            sterk["cijfer"] = True
        if not(x.isdigit() or x.isalpha()):
            sterk["speciaalkarakter"] = True
    sterkCounter = 0
    for x in sterk:
        if sterk[x] == True:
            sterkCounter +=1
    if sterkCounter == 5:
        return "sterk"
    elif sterkCounter == 3 or sterkCounter == 4:
        return "matig"
    else:
        return "zwak"


wwList = []

t = int(input(""))

for x in range(t):
    wwList.append(input())

for x in wwList:
    print(bepaalwachtwoordSterkte(x))
