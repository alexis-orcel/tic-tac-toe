import random

board = ['' for _ in range(9)]
print(f"board is now: {board}")

def insertletter(letter, pos):
    board[pos] = letter

def spaceisfree(pos):
    return board[pos] == ''

def printBoard(board):
    for i in range(3):
        for j in range(3):
            if board[3*i+j] == 'O':
                print('  O   ', end='')
            else:
                print('  ' + board[3*i+j] + '   ', end='')
            if j < 2:
                print(' ', end='')
                print('|', end=' ')
                print(' ', end='')
        print()
        if i < 2:
            print(" ---  ---  ---")


def isWinner(board, signe):
    win_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for combo in win_combinations:
        if all(board[i] == signe for i in combo):
            return True
    return False

def isBoardFull(board):
    if board.count('') > 1:
        return False
    else:
        return True

def selectRandom(li):
    return random.choice(li)

def playerMove(player):
    while True:
        move = input(f'Player {player} please select a position to place an  {player} (1-9): ')
        if move.isdigit():
            move = int(move)
            if 0 < move < 10:
                if spaceisfree(move - 1):
                    insertletter(player, move - 1)
                    break
                else:
                    print('this position is already occupied!')
            else:
                print('Please type a number within the range!')
        else:
            print('Please type a number!')

def main():
    print('Welcome to Tic Tac Toe')
    printBoard(board)
    player = 'X'
    while not (isBoardFull(board)):
        if not (isWinner(board, player)):
            playerMove(player)
            printBoard(board)
            player = 'O' if player == 'X' else 'X'
        else:
            print(f"Player {player} wins this time...")
            break
    if isBoardFull(board) and not isWinner(board, player):
        print("Game is a tie! No more spaces left to move.")


main()



