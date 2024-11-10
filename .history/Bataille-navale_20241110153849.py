import random
ai_bateaux = [["A1", "A2", "A3"],
              ["B1"],
              ["C1", "C2"]]
# Un tableau bateau
# Chaque bateau est lui meme un tableau de position
 
usr_bateaux = [["A1", "A2", "A3"],
              ["C1"],
              ["B3", "C3"]]
# Pareil pour les bateau de l'user
 
grille_usr = [["?", "?", "?"],
              ["?", "?", "?"],
              ["?", "?", "?"]]
# Grille de l'user permettant de savoir quelles cases on été essayées
# et de déterminer quels bateaux ont été touchés
# Elle sera aussi utilisé pour etre affiché
 
# Fonction qui affiche la grille de l'utilisateur
def affiche(grille):
    #parcours des lignes
    for ligne in grille:
        ligne_a_afficher='|'
        #construction de la ligne à afficher
        for pion in ligne:
            ligne_a_afficher+=pion+'|'
        print(ligne_a_afficher)
 
# Fonction du tour de l'User
def essai_usr():
     
    # On demande la case qu'il veut essayer
    inp = input("Quel casse souhaitez vous essayer ?")
 
    # Supposons que inp = "C1" alors on a les variables suivantes
    pos_x = 2
    pos_y = 0
 
    # On teste s'il n'a pas déja été essayé
    # en regardant si la case en question est un "?"
    if (grille_usr[pos_y][pos_x] != "?"):
            print("Déja tenté bro")
        essai_usr()
        # Dans ce cas on retente
   
    # Dans le cas ou la case est inconnue
    # On regarde si il y a un bateau
    if (ai_bateaux contient inp):
        ai_bateaux.remove(inp) # Si oui on retire le bateau a la position inp
 
        # Si la liste des bateaux contient des bateaux vide
        if (ai_bateaux contient [])
            # Alors un bateau viens d"etre coulé
            print("Touché coulé!")
            ai_bateaux.remove([]) # On retire les bateaux vides
        else
            # Sinon il a juste été touché car il reste des "morceaux"
            print("Touché")
 
    essai_ai() # Puis c'est au tour de l'ai
 
def essai_ai():
 
    # Pareil que pour user seul les variables sont différentes
 
    essai_usr() # Puis c'est au tour de l'user
 
# On défini le tour actuel et l'état du jeu
turn = "Usr"
isFinished = False
 
 
# On va executer le code jusqu'a ce que la partie soit terminé
while not isFinished:
 
  # Le temps que le tour est toujours a l'utilisateur
  while turn == "Usr":
    # On essaye de faire jouer l'User
    if essai_usr():
      # S'il a un tour valide on change
      turn == "AI"
    # Sinon la boucle continue
   
  # Une fois sortie de la boucle c'est a l'AI de jouer
  # Dans ce cas on est sur qu'il n'y aura pas de problème
  essai_ai()
  # Puis on redonne le tour a l'User
  turn = "Usr"
