import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# Print game board
def printBoard(board):
         print(board[0] + " | " + board[1] + " | " + board[2])
         print("----------")
         print(board[3] + " | " + board[4] + " | " + board[5])
         print("----------")
         print(board[6] + " | " + board[7] + " | " + board[8])

# Take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = currentPlayer
    else:
        print("Oops, that spot is already taken!")

#Check for win or tie
def checkgorizontal(board):
         global winner
         if board[0] == board[1] == board[2] and board[0] != "-":
             winner = board[0]
             return True
         elif board[3] == board[4] == board[5] and board[3] != "-":
                  winner = board[3]
                  return True
         elif board[6] == board[7] == board[8] and board[6] != "-":
             winner = board[6]
             return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printboard(board)
        print ("It is a tie!")
        gameRunning = False

def CheckWin():
    if checkDiag(board) or checkgorizontal(board) or checkRow(board):
        print(f"The winner is {winner}!")
    

# Switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "0"
            switchPlayer()
    



# Game loop
while gameRunning:
    printBoard(board)
    playerInput(board)
    CheckWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    CheckWin()
    checkTie(board)

         
