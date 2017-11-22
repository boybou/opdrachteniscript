# Slaapkwaliteit
# Boy Bouwense S1102301

# Vraag invoer over de tijd wanneer iemand in slaap valt en de tijd wanneer iemand minimaal wil opstaan
inSlaapValUur, inSlaapValMinuut, tenVroegsteOpstaanUur, tenVroegsteOpstaanMinuut = int(input()), int(input()), int(input()), int(input())

# Declare een constante van het aantal minuten in een dag
heleDagInMinuten = 24*60

# Reken de tijdstippen om naar minuten en
# voeg een hele dag in minuten toe aan minimale opsta tijd (maakt de berekening makkelijker)
inSlaapValTotaalMin = inSlaapValUur * 60 + inSlaapValMinuut
tenVroegsteOpstaanTotaalMin = tenVroegsteOpstaanUur*60 + tenVroegsteOpstaanMinuut + heleDagInMinuten

# Declare variable om mee te rekenen
aanbevolenOpstaTotaalMin = inSlaapValTotaalMin
# Een while loop die in sprongen van 90 minuten checkt of de minimale opsta tijd al is bereikt
while aanbevolenOpstaTotaalMin < tenVroegsteOpstaanTotaalMin:
    aanbevolenOpstaTotaalMin += 90
# Een while loop die de tijd in een 24 uur formaat houdt
while aanbevolenOpstaTotaalMin >= heleDagInMinuten:
    aanbevolenOpstaTotaalMin -= heleDagInMinuten

# Bereken aanbevolen opsta tijd
aanbevolenOpstaUur = aanbevolenOpstaTotaalMin // 60
aanbevolenOpstaTotaalMin -= aanbevolenOpstaUur * 60
aanbevolenOpstaMinuut = aanbevolenOpstaTotaalMin

# Print uitvoer
print("%0.2i:%0.2i"%(aanbevolenOpstaUur,aanbevolenOpstaMinuut))