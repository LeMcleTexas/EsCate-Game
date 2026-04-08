from plateau import *


def est_deplacement_valide_chat(plateau, ligne_depart, col_depart, ligne_arrivee, col_arrivee):
    """
    Parametres : 
                plateau : liste de liste contenant les cases
                ligne_depart,col_depart : coordonnées (x,y) de la case de depart
                ligne_arrivee,col_arrivee : coordonnées (x',y') de la case d'arrivée
    Retourne : 
                booléen si le deplacement est valide ou pas
    """
    if ligne_arrivee < 0 or ligne_arrivee > 10:
        return False
    if col_arrivee < 0 or col_arrivee > 10:
        return False
    
    if plateau[ligne_depart][col_depart] != 'C':
        return False
    
    if plateau[ligne_arrivee][col_arrivee] != '.' and plateau[ligne_arrivee][col_arrivee] != 'S':
        return False
    
    diff_ligne = abs(ligne_arrivee - ligne_depart)
    diff_col = abs(col_arrivee - col_depart)
    if diff_ligne > 1 or diff_col > 1:
        return False
    
    if diff_ligne == 0 and diff_col == 0:
        return False
    
    return True


def deplacer_chat(plateau, ligne_depart, col_depart, ligne_arrivee, col_arrivee):
    """
    Parametres : 
                plateau : liste de liste contenant les cases
                ligne_depart,col_depart : coordonnées (x,y) de la case de depart
                ligne_arrivee,col_arrivee : coordonnées (x',y') de la case d'arrivée
    Retourne :
                entier 1 si la case d'arrivée est la sortie 'S', sinon 0
    """
    pos_dep = plateau[ligne_depart][col_depart]
    pos_arr = plateau[ligne_arrivee][col_arrivee]
    actors_cible = ['O','R','W']

    if pos_dep == 'C' and pos_arr in actors_cible:
        plateau[ligne_depart][col_depart] = 'C'
        plateau[ligne_arrivee][col_arrivee] = pos_arr
        return 0
    elif pos_dep == 'C' and pos_arr == 'S':
        plateau[ligne_depart][col_depart] = '.'
        plateau[ligne_arrivee][col_arrivee] = 'S'
        return 1
    else:
        plateau[ligne_arrivee][col_arrivee] = 'C'
        plateau[ligne_depart][col_depart] = '.'
        return 0
