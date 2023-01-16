board = ['' for _ in range(9)]

def est_gagnant(board, signe):
    combinaisons_gagnantes = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for combinaison in combinaisons_gagnantes:
        if all(board[i] == signe for i in combinaison):
            return True
    return False

def grille_complete(board):
    if board.count('') > 1:
        return False
    else:
        return True

def afficher_plateau(board):
    for i in range(3):
        for j in range(3):
            print(' ' + board[3*i+j] + ' ', end='')
            if j < 2:
                print('|', end=' ')
        print()
        if i < 2:
            print(" ---  ---  ")

def tour_joueur(joueur):
    while True:
        try:
            coup = int(input("Joueur " + joueur + " veuillez sélectionner une position (1-9) : "))
            if 0 < coup < 10 and board[coup - 1] == '':
                board[coup - 1] = joueur
                break
            else:
                print('Coup non valide')
        except ValueError:
            print("Veuillez entrer un nombre!")

def main():
    print('Bienvenue dans le jeux du Tic Tac Toe')
    afficher_plateau(board)
    joueur = 'X'
    while not (grille_complete(board)):
        if not (est_gagnant(board, joueur)):
            tour_joueur(joueur)
            afficher_plateau(board)
            joueur = 'O' if joueur == 'X' else 'X'
        else:
            print("Le joueur " + joueur + " a gagné!")
            break
    if grille_complete(board) and not est_gagnant(board, joueur):
        print("Match nul!")

main()


