from plateau import *

def est_deplacement_valide_gardien(plateau, ligne_depart, col_depart, ligne_arrivee, col_arrivee):
    """ 
        Cette fonction permet de calculer si le mouvement voulu par le joueur est valide
        (Exemple : Ne pas sortir hors de la carte ou aller dans le lac).

        Elle retourne False si le mouvement est impossible et True dans le cas inverse.
    """
    if ligne_arrivee < 0 or ligne_arrivee > 10:
        return False

    if col_arrivee < 0 or col_arrivee > 10:
        return False

    if plateau[ligne_arrivee][col_arrivee] not in ['.','C','🄲']:
        return False

    diff_ligne = abs(ligne_arrivee - ligne_depart)
    diff_col = abs(col_arrivee - col_depart)

    if diff_ligne > 1 or diff_col > 1:
        return False

    if diff_ligne == 0 and diff_col == 0:
        return False

    return True


def deplacer_gardien(plateau, ligne_depart, col_depart, ligne_arrivee, col_arrivee):
    """ 
        Cette fonction permet de déplacer un gardien sur le plateau en échangeant l'état de la case 
        d'arivée et de départ.
    """

    plateau[ligne_arrivee][col_arrivee] = 'W'
    plateau[ligne_depart][col_depart] = '.'

def interaction_avec_chats(plateau, ligne_arrivee, col_arrivee, ligne_depart, col_depart):
    """ 
        Cette fonction vérifie si la case d'arrivée est un chat pour réduire le nombres de chats de 1 
        après qu'un gardien l'ai atteint.
    """

    if plateau[ligne_arrivee][col_arrivee] in ['C','🄲']:
        
        plateau[ligne_arrivee][col_arrivee] = 'W'
        plateau[ligne_depart][col_depart] = '.'
        return True
    return False


def interaction_avec_robots(plateau, ligne_arrivee, col_arrivee, ligne_depart, col_depart):
    """ 
        Cette fonction permet aux gardiens de sauter par dessus les robots. Elle calcule la 
        colonne d'arrivée et ligne d'arrivée en utilisant la formule mathématique des vecteurs
        (Vecteur = xB - xA, yB - yA). Elle remplace alors la case d'arrivée par un gardien et la
        case de départ par un '.'

        Elle retourne False si le saut a échoué et True dans le cas inverse.
    """

    if plateau[ligne_arrivee][col_arrivee] == 'R':

        vecteur_ligne = ligne_arrivee - ligne_depart
        vecteur_col = col_arrivee - col_depart

        saut_ligne = ligne_arrivee + vecteur_ligne
        saut_col = col_arrivee + vecteur_col

        if saut_ligne < 0 or saut_ligne > 10 or saut_col < 0 or saut_col > 10:
            return False

        if plateau[saut_ligne][saut_col] != '.':
            return False

        plateau[saut_ligne][saut_col] = 'W'
        plateau[ligne_depart][col_depart] = '.'

        return True
    
    return False

def teleportation(plateau, ligne_robot, col_robot, ligne_gardien, col_gardien):
    """ 
        Cette fonction permet d'échanger la place d'un robot et d'un gardien lorsque le pouvoir
        de téléportation est utilisé.

        Elle retourne True lorsque ce changement a été éffectué.
    """

    plateau[ligne_robot][col_robot] = 'W'
    plateau[ligne_gardien][col_gardien] = 'R'

    return True



