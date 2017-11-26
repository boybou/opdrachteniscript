def levensverwachting(geslacht, roker, sport, alcohol, fastfood):
    verwachteLeeftijd = 70.0
    if geslacht == "vrouw":
        verwachteLeeftijd += 4
    if roker:
        verwachteLeeftijd -= 5
    else:
        verwachteLeeftijd += 5
    if sport == 0:
        verwachteLeeftijd -= 3
    else:
        verwachteLeeftijd += sport
    if alcohol == 0:
        verwachteLeeftijd += 2
    elif alcohol > 7:
        verwachteLeeftijd -= ((alcohol-7)*0.5)
    if not(fastfood):
        verwachteLeeftijd += 3
    return verwachteLeeftijd
