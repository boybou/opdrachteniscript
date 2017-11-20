# Slaapkwaliteit
# Boy Bouwense S1102301

inSlaapValUur, inSlaapValMinuut, tenVroegsteOpstaanUur, tenVroegsteOpstaanMinuut = int(input()), int(input()), int(input()), int(input())

heleDagInMinuten = 24*60
inSlaapValTotaalMin = inSlaapValUur*60 + inSlaapValMinuut
tenVroegsteOpstaanTotaalMin = tenVroegsteOpstaanUur*60 + tenVroegsteOpstaanMinuut + heleDagInMinuten

while inSlaapValTotaalMin < tenVroegsteOpstaanTotaalMin:
    inSlaapValTotaalMin += 90
if inSlaapValTotaalMin >= heleDagInMinuten:
    inSlaapValTotaalMin -= heleDagInMinuten
aanbevolenOpstaUur = inSlaapValTotaalMin // 60
inSlaapValTotaalMin -= aanbevolenOpstaUur*60
aanbevolenOpstaMinuut = inSlaapValTotaalMin
print("%0.2i:%0.2i"%(aanbevolenOpstaUur,aanbevolenOpstaMinuut))