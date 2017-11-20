#vraag invoer van alle munt soorten
aantal1cent = int(input("aantal 1 cent munten: "))
aantal2cent = int(input("aantal 2 cent munten: "))
aantal5cent = int(input("aantal 5 cent munten: "))
aantal10cent = int(input("aantal 10 cent munten: "))
aantal20cent = int(input("aantal 20 cent munten: "))
aantal50cent = int(input("aantal 50 cent munten: "))
aantal1euro = int(input("aantal 1 euro munten: "))
aantal2euro = int(input("aantal 2 euro munten: "))
#een dictionary aanmaken voor de waardes van elke munt
waardes = {"1 cent" : 0.01,"2 cent" : 0.02,"5 cent" : 0.05, "10 cent" : 0.10, "20 cent" : 0.20, "50 cent" : 0.50, "1 euro" : 1, "2 euro" : 2}

#bereken totale waarde van alle munten
totaleWaarde = (aantal1cent*waardes["1 cent"])+(aantal2cent*waardes["2 cent"])+(aantal5cent*waardes["5 cent"])+(aantal10cent*waardes["10 cent"])+(aantal20cent*waardes["20 cent"])+(aantal50cent*waardes["50 cent"])+(aantal1euro*waardes["1 euro"])+(aantal2euro*waardes["2 euro"])
#bereken totaal aantal munten
totaalAantalMunten = aantal1cent+aantal2cent+aantal5cent+aantal10cent+aantal20cent+aantal50cent+aantal1euro+aantal2euro
#print aantal munten
print("%i munten" % totaalAantalMunten)
#print totale waarde
print("%0.2f €" % totaleWaarde)