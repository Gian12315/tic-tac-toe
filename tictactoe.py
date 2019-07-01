board = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
possibleMoves = [["7", "8", "9"],
                ["4", "5", "6"],
                ["1", "2", "3"]]

# This function prints the board... I'm unsure of how changing the width will break everything
# I should rewrite it, or fix it.                
def printBoard(board, width=10):
    print((" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2]+ " ").center(width))
    print("-" * (width + 1))
    print((" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2]+ " ").center(width))
    print("-" * (width + 1))
    print((" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2]+ " ").center(width))

# Makes a move, it checks if it's a valid move and returns true, if not, returns false
# This is probably not the best choice
def makeMove(turn, position):
    indexX = None
    indexY = None
    for list in possibleMoves:
        if position in list:
            indexX = list.index(position)
            indexY = possibleMoves.index(list)
            possibleMoves[indexY][indexX] = "0"
    if indexX is None or indexY is None:
        print ("The place is taken, pick another one")
        return False
    return True

