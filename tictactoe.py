import random

board = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]   
possibleMoves = [[7, 8, 9],
                [4, 5, 6],
                [1, 2, 3]]

# This function prints the board... I'm unsure of how changing the width will break everything
# I should rewrite it, or fix it.                
def printBoard(board, width=10):
    print((" " + str(board[0][0]) + " | " + str(board[0][1]) + " | " + str(board[0][2]) + " ").center(width))
    print("-" * (width + 1))
    print((" " + str(board[1][0]) + " | " + str(board[1][1]) + " | " + str(board[1][2]) + " ").center(width))
    print("-" * (width + 1))
    print((" " + str(board[2][0]) + " | " + str(board[2][1]) + " | " + str(board[2][2]) + " ").center(width))

# Makes a move, it checks if it's a valid move and returns true, if not, returns false
# This is probably not the best choice
def makeMove(turn, position):
    indexX = None
    indexY = None
    for list in possibleMoves:
        if position in list:
            indexX = list.index(position)
            indexY = possibleMoves.index(list)
            possibleMoves[indexY][indexX] = "/"
            board[indexY][indexX] = turn
    if indexX is None or indexY is None:
        print ("The place is taken, pick another one")
        return False
    return True

def gameLoop():
    print("Tic Tac Toe Game")
    turn = random.choice(["X","O"])
    hasWon = False
    position = None
    while hasWon is not True:
        printBoard(board)    
        print("\n\nIs {} turn.".format(turn))
        try:
            position = int(input("Position: "))
        except Exception as err:
            print("Please, insert a valid number")
            position = 0
        if not (position >=1 and position <=9):
            print("Invalid move, please insert one of these values")
            printBoard(possibleMoves)

        isValid = makeMove(turn, position)
        if isValid is not True:
            continue
        hasWon = checkIfWon(turn, board) 
        if hasWon is True:
            printBoard(board)
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

def checkIfWon(turn, board):
    # This checks horizontal
    for lists in board:
        if lists.count(turn) == 3:
            print ("{} has won!".format(turn))
            return True
    # This checks for vertical
    for x in range(3):
        ocurrences = 0
        for y in range(3):
            if board[y][x] == turn:
                ocurrences = ocurrences + 1
        if ocurrences == 3:
            print ("{} has won!".format(turn))
            return True
    # This checks for diagonal
    if (board[0][0] == turn and board[1][1] == turn and board[2][2] == turn) or \
    (board[0][2] == turn and board[1][1] == turn and board[2][0] == turn):
        print ("{} has won!".format(turn))
        return True
    return False

gameLoop()
