#vraag invoer aantal sol
aantalSol = int(input("aantal sol: "))

#aantal seconden in 1 sol
aantalseconden1sol = 24*60*60 + 39*60 + 35.244

#zet aantal sol om naar seconden
totaalSeconden = aantalseconden1sol * aantalSol
#bereken aantal dagen
aantalDagen = totaalSeconden/60/60//24
#bereken resterende seconden
totaalSeconden = totaalSeconden - aantalDagen*24*60*60
#bereken aantal uren
aantalUren = totaalSeconden/60//60
#bereken resterende seconden
totaalSeconden = totaalSeconden - aantalUren*60*60
#bereken aantal minuten
aantalMinuten = totaalSeconden//60
#bereken resterende seconden
totaalSeconden = totaalSeconden - aantalMinuten*60
#bereken aantal seconden
aantalseconden = round(totaalSeconden,0)

#print het resultaat
print("%i sol = %i dagen, %i uren, %i minuten en %i seconden" % (aantalSol,aantalDagen,aantalUren,aantalMinuten,aantalseconden))



