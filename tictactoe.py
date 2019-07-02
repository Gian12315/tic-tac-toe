import random

board = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]   
pM = [[7, 8, 9],
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
    for list in pM:
        if position in list:
            indexX = list.index(position)
            indexY = pM.index(list)
            pM[indexY][indexX] = 0
            board[indexY][indexX] = turn
    if indexX is None or indexY is None:
        print ("The place is taken, pick another one")
        return False
    return True

def gameLoop():
    print("Tic Tac Toe Game")
    print("-" * 20)
    print("How to play")
    print("Input one of the possible positions to pick one of them.")
    printBoard(pM)
    print("-" * 20)
    choice = int(input("1. Play against a friend \n2. Play against IA\n"))
    turn = random.choice(["X","O"])
    hasWon = False
    position = None
    turns = 0
    if choice == 1:
        while hasWon is not True:
            printBoard(board)    
            print("\n\nIs {} turn.".format(turn))
            position = getMove()

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
            turns += 1
            if turns == 9:
                break
    elif choice == 2:
        while hasWon is not True:
            print("\n\n\n")
            printBoard(board)
            if turn == "X":
                position = getMove()
                isValid = makeMove(turn, position)
                if isValid is not True:
                    continue
            elif turn == "O":
                iaTurn()
            hasWon = checkIfWon(turn, board) 
            if hasWon is True:
                printBoard(board)
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            turns += 1
            if turns == 9:
                break

    else:
        raise Exception("Invalid choice, please run the program again.")
    print("\n\n\n\n")
    printBoard(board)
    print("The board is full, tie!")

def getMove():
    try:
        position = int(input("Position: "))
    except Exception as err:
        print("Please, insert a valid number")
        position = 0
    if not (position >=1 and position <=9):
        print("Invalid move, please insert one of these values")
        printBoard(pM)
    return position

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

def iaTurn():
    center = pM[1][1]
    corners = [pM[0][0], pM[0][2], pM[2][0], pM[2][2]]
    corners.sort()
    fullCorners = corners.count(0)
    sides = [pM[0][1], pM[1][0], pM[1][2], pM[2][1]]
    sides.sort()
    fullSides = sides.count(0)
    if center != 0:
        pM[1][1] = 0
        board[1][1] = "O"
        return True
    elif fullCorners != 4:
        for i in range(fullCorners):
            corners.remove(0)
        randomCorner = random.choice(corners)
        if isinstance(randomCorner, int):
            for list in pM:
                if randomCorner in list:
                    indexX = list.index(randomCorner)
                    indexY = pM.index(list)
                    pM[indexY][indexX] = 0
                    board[indexY][indexX] = "O"
        return True
    else:
        for i in range(fullSides):
            sides.remove(0)
        randomSide = random.choice(sides)
        if isinstance(randomSide, int):
            for list in pM:
                if randomSide in list:
                    indexX = list.index(randomSide)
                    indexY = pM.index(list)
                    pM[indexY][indexX] = 0
                    board[indexY][indexX] = "O"
        return True
    return False
        

gameLoop()
