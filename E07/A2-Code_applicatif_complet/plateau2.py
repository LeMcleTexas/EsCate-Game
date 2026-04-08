import random

def creer_plateau():
    """
    Retourne :
                plateau : une liste de liste 11x11 vide, soit rempli de '.'
    """
    plateau = []
    for i in range(11):
        ligne = []
        for j in range(11):
            ligne.append('.')
        plateau.append(ligne)
    return plateau


def placer_elements_initiaux(plateau):
    """
    Parametres :
                plateau
    Retourne :
               Modifie le plateau avec les acteurs initialisés dedans tous fixe sauf les Robots aleatoire
    """
    plateau[0][5] = 'S'
    plateau[3][0] = 'C'
    plateau[4][0] = 'S'
    plateau[4][10] = 'S'
    
    plateau[2][4] = 'O'
    plateau[2][5] = 'O'
    plateau[2][6] = 'O'
    plateau[3][4] = 'O'
    plateau[3][5] = 'O'
    plateau[3][6] = 'O'
    
    plateau[1][2] = 'W'
    plateau[0][3] = 'C'
    plateau[1][8] = 'W'
    plateau[1][7] = 'C'
    plateau[2][8] = '🄲'

    nb_robots_places = 0
    while nb_robots_places < 9:
        l = random.randint(0, 10)
        c = random.randint(0, 10)
        if plateau[l][c] == '.':
            plateau[l][c] = 'R'
            nb_robots_places += 1

def afficher_plateau(plateau):
    """
    Parametre :
                Plateau
    Retourne :
                Affiche le plateau avec une interface colonne A-K, ligne 1-11
    """
    print("\n   A B C D E F G H I J K")
    for i in range(11):
        numero_ligne = i + 1
        if numero_ligne < 10:
            print(str(numero_ligne) + "  ", end="")
        else:
            print(str(numero_ligne) + " ", end="")
        for j in range(11):
            print(plateau[i][j] + " ", end="")
        print()
    print()


def convertir_colonne_en_index(colonne):
    """
    Passe les lettres des colonnes en indices
    """
    colonne = colonne.upper()
    if colonne == 'A':
        return 0
    elif colonne == 'B':
        return 1
    elif colonne == 'C':
        return 2
    elif colonne == 'D':
        return 3
    elif colonne == 'E':
        return 4
    elif colonne == 'F':
        return 5
    elif colonne == 'G':
        return 6
    elif colonne == 'H':
        return 7
    elif colonne == 'I':
        return 8
    elif colonne == 'J':
        return 9
    elif colonne == 'K':
        return 10
    else:
        return -1

