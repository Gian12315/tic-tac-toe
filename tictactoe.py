board = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

def printBoard(board, width=10):
    print((" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2]+ " ").center(width))
    print("-" * (width + 1))
    print((" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2]+ " ").center(width))
    print("-" * (width + 1))
    print((" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2]+ " ").center(width))
printBoard(board)