def T9(woord):
    toets2 = ["a","b","c"]
    toets3 = ["d","e","f"]
    toets4 = ["g","h","i"]
    toets5 = ["j","k","l"]
    toets6 = ["m", "n", "o"]
    toets7 = ["p", "q", "r", "s"]
    toets8 = ["t", "u", "v"]
    toets9 = ["w", "x", "y", "z"]

    toetsen = [toets2, toets3, toets4, toets5, toets6, toets7, toets8, toets9]
    cijferCombinatie = ''
    for x in woord:
        for y in toetsen:
            if x.lower() in y:
                cijferCombinatie += str(toetsen.index(y)+2)
    return cijferCombinatie


def GSMoniemen(woord1, woord2):
    if T9(woord1) == T9(woord2):
        return True
    else:
        return False
