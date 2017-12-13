# Forsyth-Edwards notatie
# Boy Bouwense s1102301


def fen2grid(FEN_string,lveld="*"):
    return_string = ""
    for x in FEN_string:
        if x == "/":
            return_string += "\n"
        elif x.isdigit():
            for b in range(int(x)):
                return_string += lveld
        else:
            return_string += x
    return return_string


def grid2fen(grid_string,lvel="*"):
    return_string = ""
    temp_number = 0
    number_last = False
    for x in grid_string:
        if x == lvel:
            temp_number += 1
            number_last = True
        elif x == "\n":
            if number_last:
                return_string += str(temp_number)
                temp_number = 0
                number_last = False
            return_string += "/"
        else:
            if number_last:
                return_string += str(temp_number)
                temp_number = 0
                number_last = False
            return_string += x
    return return_string


def main():
    print(fen2grid('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'),"\n")
    print(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR', '.'),"\n")
    print(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '+'),"\n")
    rooster = '''rnbqkbnr\npppppppp\n********\n********\n********\n********\nPPPPPPPP\nRNBQKBNR'''
    print(grid2fen(rooster),"\n")
    print(grid2fen(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR')),"\n")
    print(grid2fen(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '.'), '.'),"\n")
    print(grid2fen(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R', '+'), '+'),"\n")


if __name__ == "__main__":
    main()