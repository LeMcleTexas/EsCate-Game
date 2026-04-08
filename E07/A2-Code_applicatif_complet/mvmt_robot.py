import random

# Liste des déplacements possibles (Haut, Bas, Gauche, Droite)
# Les robots ne se déplacent pas en diagonale.
DEPLACEMENTS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

def trouver_robots(plateau):
    """
    Parametres :
                plateau : liste de liste 11x11 représentant la grille de jeu
    Retourne :
                robots : une liste de tuples (ligne, col) correspondant aux coordonnées des robots
    """
    robots = []
    for i in range(11):
        for j in range(11):
            if plateau[i][j] == 'R':
                robots.append((i, j))
    return robots


def deplacement_possible(plateau, ligne, col, new_ligne, new_col):
    """
    Parametres :
                plateau : la grille de jeu
                ligne, col : coordonnées actuelles du robot (non utilisées dans la vérification mais présentes en paramètre)
                new_ligne, new_col : coordonnées de la destination visée
    Retourne :
                booléen : True si le déplacement est autorisé, False sinon
    """

    if new_ligne < 0 or new_ligne > 10:
        return False
    if new_col < 0 or new_col > 10:
        return False

    case = plateau[new_ligne][new_col]

    if case in ['O', 'S', 'R', 'C', 'W']:
        return False

    return True


def deplacer_robots(plateau):
    """
    Parametres :
                plateau : la grille de jeu (modifiée en place)
    Retourne :
                Rien (modifie directement le plateau)
    """
    robots = trouver_robots(plateau)

    for (ligne, col) in robots:

        if random.randint(1, 3) != 1:
            continue

        random.shuffle(DEPLACEMENTS)
        a_bouge = False

        for d_ligne, d_col in DEPLACEMENTS:
            new_ligne = ligne + d_ligne
            new_col = col + d_col

            if deplacement_possible(plateau, ligne, col, new_ligne, new_col):
                plateau[new_ligne][new_col] = 'R'
                plateau[ligne][col] = '.'
                a_bouge = True
                break

        if not a_bouge:
            continue

