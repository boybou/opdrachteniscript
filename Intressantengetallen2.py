import datetime
import time
def tel_losse_numers_naar_getal(getal):
    totaal = 0
    getal_string = str(getal)

    for x in range (len(getal_string)):
        totaal += int(getal_string[x])
    return int(totaal)

aantal_testgetallen = int(input())
testgetallen = []

for x in range (0, aantal_testgetallen):
    testgetallen.append(int(input()))
print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
teller = 0
getal = 0
gevonden = False
for teller in range(0, len(testgetallen)):
    while not gevonden:
        if getal % testgetallen[teller] == 0:
            if testgetallen[teller] == tel_losse_numers_naar_getal(getal):
                print ("gevonden %i" % getal)
                gevonden = True

        getal += 1
print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))