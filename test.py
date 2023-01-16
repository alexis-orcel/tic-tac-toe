import random

board = ['' for _ in range(9)]

def is_winner(board, signe):
    win_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for combo in win_combinations:
        if all(board[i] == signe for i in combo):
            return True
    return False

def is_board_full(board):
    if board.count('') > 1:
        return False
    else:
        return True

def print_board(board):
    for i in range(3):
        for j in range(3):
            print(f' {board[3*i+j]} ', end='')
            if j < 2:
                print('|', end=' ')
        print()
        if i < 2:
            print(" ---  ---  ---")

def player_move(player):
    while True:
        try:
            move = int(input(f'Player {player} please select a position (1-9): '))
            if 0 < move < 10 and board[move - 1] == '':
                board[move - 1] = player
                break
            else:
                print('Invalid move')
        except ValueError:
            print("Please type a number!")

def main():
    print('Welcome to Tic Tac Toe')
    print_board(board)
    player = 'X'
    while not (is_board_full(board)):
        if not (is_winner(board, player)):
            player_move(player)
            print_board(board)
            player = 'O' if player == 'X' else 'X'
        else:
            print(f"Player {player} wins!")
            break
    if is_board_full(board) and not is_winner(board, player):
        print("Game is a tie!")

main()
