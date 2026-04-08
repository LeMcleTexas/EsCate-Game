from plateau import *

def est_deplacement_valide_special(plateau, ligne_depart, col_depart, ligne_arrivee, col_arrivee):
    """
    Paramètres :
    plateau (list) : plateau de jeu représentant l'état actuel du jeu
    ligne_depart (int) : indice de la ligne de départ du chat spécial
    col_depart (int) : indice de la colonne de départ du chat spécial
    ligne_arrivee (int) : indice de la ligne d'arrivée souhaitée
    col_arrivee (int) : indice de la colonne d'arrivée souhaitée

    Retour :
    bool : True si le déplacement est valide, False sinon
    """
    if ligne_arrivee < 0 or ligne_arrivee > 10:
        return False
    if col_arrivee < 0 or col_arrivee > 10:
        return False
    
    if plateau[ligne_depart][col_depart] != '🄲':
        return False
    
    if plateau[ligne_arrivee][col_arrivee] != '.' and plateau[ligne_arrivee][col_arrivee] != 'S':
        return False
    
    diff_ligne = abs(ligne_arrivee - ligne_depart)
    diff_col = abs(col_arrivee - col_depart)
    if diff_ligne > 2 or diff_col > 2:
        return False
    
    if diff_ligne == 0 and diff_col == 0:
        return False
    
    return True


def deplacer_chat_special(plateau, ligne_depart, col_depart, ligne_arrivee, col_arrivee):
    """
    Paramètres :
    plateau (list) : plateau de jeu représentant l'état actuel du jeu
    ligne_depart (int) : indice de la ligne de départ du chat spécial
    col_depart (int) : indice de la colonne de départ du chat spécial
    ligne_arrivee (int) : indice de la ligne d'arrivée du chat spécial
    col_arrivee (int) : indice de la colonne d'arrivée du chat spécial

    Retour :
    None
    """
    pos_dep = plateau[ligne_depart][col_depart]
    pos_arr = plateau[ligne_arrivee][col_arrivee]
    actors_cible = ['O','R','W']

    if pos_dep == '🄲' and pos_arr in actors_cible:
        plateau[ligne_depart][col_depart] = '🄲'
        plateau[ligne_arrivee][col_arrivee] = pos_arr
        return 0
    elif pos_dep == '🄲' and pos_arr == 'S':
        plateau[ligne_depart][col_depart] = '.'
        plateau[ligne_arrivee][col_arrivee] = 'S'
        return 1
    else:
        plateau[ligne_arrivee][col_arrivee] = '🄲'
        plateau[ligne_depart][col_depart] = '.'
        return 0
