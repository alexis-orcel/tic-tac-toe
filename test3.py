import random

#Conception D'un Tableau
board = ['' for _ in range(9)]
print(f"board is now: {board}")

def insertletter(letter, pos):
    board[pos] = letter

def spaceisfree(pos):
    return board[pos] == ''

def printBoard(board):
    for i in range(1):
        print('  |   |')
        print(' ' + board[3*i] + ' |  ' + board[3*i+1] + ' | ' + board[3*i+2])
        print('  |   |')
        if i < 2:
            print('----------')

#Savoir si le joueur gagne
def isWinner(board, signe):
    win_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for combo in win_combinations:
        if all(board[i] == signe for i in combo):
            return True
    return False

#grille complete fin du jeux
def isBoardFull(board):
    if board.count('') > 1:
        return False
    else:
        return True











printBoard(board)









