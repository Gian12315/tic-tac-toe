import random, copy

board = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]   
pM =            [[7, 8, 9],
                [4, 5, 6],
                [1, 2, 3]]

def getBoard():
    return board
def setBoard(newBoard):
    board = copy.deepcopy(newBoard)
    return board

# This function prints the board... I'm unsure of how changing the width will break everything            
def printBoard(board, width=10):
    print((" " + str(board[0][0]) + " | " + str(board[0][1]) + " | " + str(board[0][2]) + " ").center(width))
    print("-" * (width + 1))
    print((" " + str(board[1][0]) + " | " + str(board[1][1]) + " | " + str(board[1][2]) + " ").center(width))
    print("-" * (width + 1))
    print((" " + str(board[2][0]) + " | " + str(board[2][1]) + " | " + str(board[2][2]) + " ").center(width))

# Makes a move, it checks if it's a valid move and returns true, if not, returns false
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

# The game main loop.
def gameLoop():
    print("Tic Tac Toe Game")
    print("-" * 20)
    print("How to play")
    print("Input one of the possible positions to pick one of them.")
    printBoard(pM)
    print("-" * 20)
    choice = int(input("1. Play against a friend \n2. Play against IA\n3. Play against expert IA\n"))
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
            hasWon = bool(checkIfWon(turn, board))
            if hasWon is True:
                print ("{} has won!".format(turn))
                printBoard(board)
                return
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
            hasWon = bool(checkIfWon(turn, board) )
            if hasWon is True:
                print ("{} has won!".format(turn))
                printBoard(board)
                return
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            turns += 1
            if turns == 9:
                break
    elif choice == 3:
        while hasWon is not True:
            print("\n\n\n")
            printBoard(board)
            if turn == "X":
                position = getMove()
                isValid = makeMove(turn, position)
                if isValid is not True:
                    continue
            elif turn == "O":
                perfectIaTurn()
            hasWon = bool(checkIfWon(turn, board) )
            if hasWon is True:
                print ("{} has won!".format(turn))
                printBoard(board)
                return
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

# Gets an input and checks if the move is between the possible values, if not it returns 0.
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
            return 1
    # This checks for vertical
    for x in range(3):
        ocurrences = 0
        for y in range(3):
            if board[y][x] == turn:
                ocurrences = ocurrences + 1
        if ocurrences == 3:
            return 1
    # This checks for diagonal
    if (board[0][0] == turn and board[1][1] == turn and board[2][2] == turn) or \
    (board[0][2] == turn and board[1][1] == turn and board[2][0] == turn):
        return 1
    return 0

# Tries to take the center, or a random corner and finally a random side.
def iaTurn():
    center = pM[1][1]
    corners = [pM[0][0], pM[0][2], pM[2][0], pM[2][2]]
    corners.sort()
    sides = [pM[0][1], pM[1][0], pM[1][2], pM[2][1]]
    sides.sort()
    fullCorners = corners.count(0)
    fullSides = sides.count(0)
    if center != 0:
        pM[1][1] = 0
        board[1][1] = "O"
    elif fullCorners != 4:
        for i in range(0, fullCorners):
            corners.remove(0)
        randomCorner = random.choice(corners)
        if isinstance(randomCorner, int):
            for list in pM:
                if randomCorner in list:
                    indexX = list.index(randomCorner)
                    indexY = pM.index(list)
                    pM[indexY][indexX] = 0
                    board[indexY][indexX] = "O"
    else:
        for i in range(0, fullSides):
            sides.remove(0)
        randomSide = random.choice(sides)
        if isinstance(randomSide, int):
            for list in pM:
                if randomSide in list:
                    indexX = list.index(randomSide)
                    indexY = pM.index(list)
                    pM[indexY][indexX] = 0
                    board[indexY][indexX] = "O"

# Tries to find a game winning move, if not possible, it calls iaTurn()
def perfectIaTurn():
    remaining = {}
    for lista in pM:
        for element in lista:
            if element == 0:
                continue
            indexX = lista.index(element)
            indexY = pM.index(lista)
            remaining.setdefault(element, [indexY, indexX])
    canWin = True
    for i in range(0, 2):
        for key in remaining.keys():
            coords = remaining[key]
            y = coords[0]
            x = coords[1]
            testBoard = copy.deepcopy(getBoard())
            testBoard[y][x] = "O"
            result = checkIfWon("O", testBoard)
            if canWin:
                if result == 1:
                    board[y][x] = "O"
                    pM[y][x] = 0
                    return True
                elif result == 0:
                    continue
            else:
                iaTurn()
                return True
        canWin = False
        
gameLoop()
