yAs = [1, 2, 3, 4, 5, 6, 7, 8]
xAs = [ord('a'), ord('b'), ord('c'), ord('d'), ord('e'), ord('f'), ord('g'), ord('h')]

inputString1 = input("begin positie: ")
inputString2 = input("bestemmings positie: ")

beginx = ord(inputString1[0])
beginy = int(inputString1[1])
bestemmingx = ord(inputString2[0])
bestemmingy = int(inputString2[1])

def checkPaardenSprong(beginx, beginy, bestemmingx, bestemmingy):
    if (beginx in xAs) and (beginy in yAs) and (bestemmingy in yAs) and (bestemmingx in xAs):
        if (bestemmingx == (beginx + 2)) and (bestemmingy == (beginy - 1) or bestemmingy == (beginy + 1)):
            print("het paard kan springen van %s naar %s" % (inputString1,inputString2))
            return
        elif (bestemmingx == (beginx - 2)) and (bestemmingy == (beginy - 1) or bestemmingy == (beginy + 1)):
            print("het paard kan springen van %s naar %s" % (inputString1,inputString2))
            return
        elif (bestemmingy == (beginy + 2)) and (bestemmingx == (beginx - 1) or bestemmingx == (beginx + 1)):
            print("het paard kan springen van %s naar %s" % (inputString1,inputString2))
            return
        elif (bestemmingy == (beginy - 2)) and (bestemmingx == (beginx - 1) or bestemmingx == (beginx + 1)):
            print("het paard kan springen van %s naar %s" % (inputString1,inputString2))
            return
        else:
            print("het paard kan niet springen van %s naar %s" % (inputString1,inputString2))
            return
    else:
        print("een van de ingevoerde posities ligt niet op het schaakbord")
        return

checkPaardenSprong(beginx, beginy, bestemmingx, bestemmingy)



# y+2 x-1||x+1
# y-2 x-1||x+1
# x+2 y-1||y+1
# x-2 y-1||y+1
