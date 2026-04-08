from plateau import *
from plateau2 import *
from mvmt_chat import *
from mvmt_chat_special import *
from mvmt_robot import *
from interactions_gardiens import *

print("=== Configuration de la partie ===")
print("plateau : Mode Normale (début classique)")
print("plateau2 : Mode Démo (peu de chats)")

choix = ""
while choix not in ["plateau", "plateau2"]:
    choix = input("Tu dois choisir entre plateau et plateau2 : ")

if choix == "plateau":
    print("\n"*50)
    from plateau import *
else:
    print("\n"*50)
    from plateau2 import *

def compter_chats(plateau):
    """
    Parametre:
                plateau
    Retourne:
                entier, nombre de chats et chats special
    """
    compteur = 0
    for ligne in plateau:
        for case in ligne:
            if(case in ['C','🄲']):
                compteur+=1
    return compteur

def main():
    print("=== Jeu EsCATe Game ===")
    
    score_joueur1 = 0
    score_joueur2 = 0

    for num_manche in range(1, 3):
        print("\n" + "="*40)
        print("=== DEBUT DE LA MANCHE "+str(num_manche)+" ===")
        print("="*40)

        if num_manche == 1:
            print("Joueur 1 : CHATS | Joueur 2 : GARDIENS")
            joueur_chat = "Joueur 1"
        else:
            print("Joueur 2 : CHATS | Joueur 1 : GARDIENS")
            joueur_chat = "Joueur 2"

        plateau = creer_plateau()
        placer_elements_initiaux(plateau)
        
        score_manche_chats = 0
        

        while compter_chats(plateau) > 0:
            
            print("\n--- Tour de "+str(joueur_chat)+" (Chats) ---")
            afficher_plateau(plateau)

            nb_chats_sur_plateau = compter_chats(plateau)
            nb_deplacements_a_faire = min(7, nb_chats_sur_plateau)
            
            chats_deplaces = 0
            chats_ko_tour = [] 
            erreur = False

            #Phase 1 : Chats

            while chats_deplaces < nb_deplacements_a_faire:
                if compter_chats(plateau) == 0:
                    break

                if not erreur:
                    print("Chat numéro "+str(chats_deplaces+1)+" sur "+str(nb_deplacements_a_faire))
                else:
                    afficher_plateau(plateau)

                ligne_depart_str = input("  Ligne du Chat à déplacer (1-11) : ")
                col_depart_str = input("  Colonne du Chat à déplacer (A-K) : ")
            
                if ligne_depart_str.strip() == "" or col_depart_str.strip() == "":
                    print("\n"*50)
                    print(">> Erreur : Champs vides !")
                    erreur = True
                    continue

                if ligne_depart_str not in [str(i) for i in range(1, 12)]:
                    print("\n"*50)
                    print(">> Erreur : Ligne invalide !")
                    erreur = True
                    continue

                ligne_depart = int(ligne_depart_str) - 1
                col_depart = convertir_colonne_en_index(col_depart_str)
            
                if col_depart == -1:
                    print("\n" * 50)
                    print(">> Erreur : Colonne invalide !")
                    erreur = True
                    continue

                if (ligne_depart, col_depart) in chats_ko_tour:
                    print("\n" * 50)
                    print(">> Erreur : Ce chat a déjà bougé ce tour-ci !")
                    erreur = True
                    continue
                
                if plateau[ligne_depart][col_depart] not in ['C','🄲']:
                    print("\n" * 50)
                    print(">> Erreur : Pas de chat à cette position !")
                    erreur = True
                    continue

                while True:
                    ligne_arrivee_str = input("  Ligne d'arrivée (1-11) : ")
                    col_arrivee_str = input("  Colonne d'arrivée (A-K) : ")
                    
                    if ligne_arrivee_str not in [str(i) for i in range(1, 12)]:
                        print("\n" * 50)
                        print(">> Erreur : Ligne invalide.")
                        continue
                    
                    col_arrivee = convertir_colonne_en_index(col_arrivee_str)
                    if col_arrivee == -1:
                        print("\n" * 50)
                        print(">> Erreur : Colonne invalide.")
                        continue
                    
                    ligne_arrivee = int(ligne_arrivee_str) - 1
                    break
                
                if plateau[ligne_depart][col_depart] == 'C':
                    if not est_deplacement_valide_chat(plateau, ligne_depart, col_depart, ligne_arrivee, col_arrivee):
                        print("\n" * 50)
                        print(">> Mouvement invalide (trop loin, obstacle ou occupé).")
                        erreur = True
                        continue
                    points_gagnes = deplacer_chat(plateau, ligne_depart, col_depart, ligne_arrivee, col_arrivee)
                    

                if plateau[ligne_depart][col_depart] == '🄲':
                    if not est_deplacement_valide_special(plateau, ligne_depart, col_depart, ligne_arrivee, col_arrivee):
                        print("\n"*50)
                        print(">> Mouvement invalide (trop loin, obstacle ou occupé).")
                        erreur = True
                        continue
                    points_gagnes = deplacer_chat_special(plateau, ligne_depart, col_depart, ligne_arrivee, col_arrivee)


                score_manche_chats += points_gagnes
                
                chats_deplaces += 1
                erreur = False
                
                if plateau[ligne_arrivee][col_arrivee] in ['C','🄲']:
                    chats_ko_tour.append((ligne_arrivee, col_arrivee))

                print("\n"*50)
                afficher_plateau(plateau)

            if compter_chats(plateau) == 0:
                print("\nTous les chats sont sortis ou capturés !")
                break

            print("\n--- Tour des Gardiens ---")
            gardiens_deplaces = 0
            magie = 3
            gardiens_bloques_tour = []
            erreur = False

            #Phase 2 : Gardiens

            while gardiens_deplaces < 2:
                if not erreur:
                    print("Gardien numéro "+str(gardiens_deplaces+1)+" sur 2")
                else:
                    afficher_plateau(plateau)


                if magie > 0 and not erreur:
                    choix_tp = input("Utiliser téléportation (oui/non) ? : ")

                    while choix_tp not in ["oui", "non"]:
                        print("Ce n'est pas une réponse valable")
                        choix_tp = input("Utiliser téléportation (oui/non) ? : ")

                    if choix_tp == "oui":

                        choix_ligne_robot = int(input("Ligne du Robot : ")) - 1
                        choix_colonne_robot = convertir_colonne_en_index(input("Colonne du Robot : "))

                        choix_lhigne_gardien = int(input("Ligne du Gardien : ")) - 1
                        choix_colonne_gardien = convertir_colonne_en_index(input("Colonne du Gardien : "))

                        if plateau[choix_ligne_robot][choix_colonne_robot] == 'R' and plateau[choix_lhigne_gardien][choix_colonne_gardien] == 'W':
                            teleportation(plateau, choix_ligne_robot, choix_colonne_robot, choix_lhigne_gardien, choix_colonne_gardien)
                            magie -= 1
                            gardiens_deplaces += 1
                            gardiens_bloques_tour.append((choix_ligne_robot, choix_colonne_robot))
                            afficher_plateau(plateau)
                            continue
                        else:
                            print("Erreur : Coordonnées invalides (pas un Robot ou pas un Gardien).") 

                ligne_depart_str = input("  Ligne du Gardien (1-11) : ")
                col_depart_str = input("  Colonne du Gardien (A-K) : ")
                
                if ligne_depart_str not in [str(i) for i in range(1, 12)]:
                    print("\n" * 50)
                    print(">> Erreur : Ligne invalide !")
                    erreur = True
                    continue

                ligne_depart = int(ligne_depart_str) - 1
                col_depart = convertir_colonne_en_index(col_depart_str)
            
                if col_depart == -1 or plateau[ligne_depart][col_depart] != 'W':
                    print("\n" * 50)
                    print(">> Erreur : Sélectionnez une case avec un Gardien (W) !")
                    erreur = True
                    continue

                if (ligne_depart,col_depart) in gardiens_bloques_tour:
                    print("\n" * 50)
                    print(">> Erreur : Ce gardien a déjà bougé ce tour !")
                    erreur = True
                    continue

                while True:
                    ligne_arrivee_str = input("  Ligne d'arrivée (1-11) : ")
                    col_arrivee_str = input("  Colonne d'arrivée (A-K) : ")
                    
                    if ligne_arrivee_str in [str(i) for i in range(1, 12)]:
                        ligne_arrivee = int(ligne_arrivee_str) - 1
                        col_arrivee = convertir_colonne_en_index(col_arrivee_str)
                        if col_arrivee != -1:
                            break
                    print(">> Erreur : Destination invalide.")

                action_reussie = False 

                if interaction_avec_robots(plateau, ligne_arrivee, col_arrivee, ligne_depart, col_depart):
                    action_reussie = True
                elif interaction_avec_chats(plateau, ligne_arrivee, col_arrivee, ligne_depart, col_depart):
                    action_reussie = True
                elif est_deplacement_valide_gardien(plateau, ligne_depart, col_depart, ligne_arrivee, col_arrivee):
                    deplacer_gardien(plateau, ligne_depart, col_depart, ligne_arrivee, col_arrivee)
                    action_reussie = True
                else:
                    print("\n" * 50)
                    print(">> Mouvement impossible.")
                    erreur = True
                    continue

                if action_reussie:
                    gardiens_deplaces += 1
                    gardiens_bloques_tour.append((ligne_arrivee,col_arrivee))
                    erreur = False
                    print("\n"*50)
                    afficher_plateau(plateau)

            print("\n"*50)
            if compter_chats(plateau) == 0:
                print("\nTous les chats ont été capturés par les gardiens !")
                break

            #Phase 3 : Robots
            print("---Phase Robots---")
            afficher_plateau(plateau)
            deplacer_robots(plateau)
            print("Les robots ont étés deplacés !")

        print("\nFin de la manche "+str(num_manche)+".")
        print("Score réalisé par les chats cette manche : "+str(score_manche_chats))
        
        if num_manche == 1:
            score_joueur1 += score_manche_chats
        else:
            score_joueur2 += score_manche_chats

    print("\n" + "="*40)
    print("=== FIN DE LA PARTIE ===")
    print("Score Joueur 1 : "+str(score_joueur1))
    print("Score Joueur 2 : "+str(score_joueur2))
    
    if score_joueur1 > score_joueur2:
        print("VICTOIRE DU JOUEUR 1 !")
    elif score_joueur2 > score_joueur1:
        print("VICTOIRE DU JOUEUR 2 !")
    else:
        print("EGALITE !")
    print("="*40)

if __name__ == "__main__":
    main()
