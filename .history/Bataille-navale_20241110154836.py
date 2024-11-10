def affiche(grille):
    #parcours des lignes
    for ligne in grille:
        ligne_a_afficher='|'
        #construction de la ligne à afficher
        for pion in ligne:
            ligne_a_afficher+=pion+'|'
        print(ligne_a_afficher)
 
grille_joueur=[["  ","A","B","C","D","E","F","G","H","I","J"],    #Grille affiché, ce que le joueur voit
        ["01"," "," "," "," "," "," "," "," "," "," "],
        ["02"," "," "," "," "," "," "," "," "," "," "],
        ["03"," "," "," "," "," "," "," "," "," "," "],
        ["04"," "," "," "," "," "," "," "," "," "," "],
        ["05"," "," "," "," "," "," "," "," "," "," "],
        ["06"," "," "," "," "," "," "," "," "," "," "],
        ["07"," "," "," "," "," "," "," "," "," "," "],
        ["08"," "," "," "," "," "," "," "," "," "," "],
        ["09"," "," "," "," "," "," "," "," "," "," "],
        ["10"," "," "," "," "," "," "," "," "," "," "]]
 
grille_ordi=[["  ","A","B","C","D","E","F","G","H","I","J"],    #Deuxième grille affiché, ce que le joueur voit
        ["01"," "," "," "," "," "," "," "," "," "," "],
        ["02"," "," "," "," "," "," "," "," "," "," "],
        ["03"," "," "," "," "," "," "," "," "," "," "],
        ["04"," "," "," "," "," "," "," "," "," "," "],
        ["05"," "," "," "," "," "," "," "," "," "," "],
        ["06"," "," "," "," "," "," "," "," "," "," "],
        ["07"," "," "," "," "," "," "," "," "," "," "],
        ["08"," "," "," "," "," "," "," "," "," "," "],
        ["09"," "," "," "," "," "," "," "," "," "," "],
        ["10"," "," "," "," "," "," "," "," "," "," "]]
 
compteur=0 #Initialisation du compteur
navires=[" "," "," "," "," "," "]
navires[1]=5  #Porte-avion (5 cases)
navires[2]=4  #Cuirasier (4 cases)
navires[3]=3  #Fregate (3 cases)
navires[4]=3  #Sous-marin (3 cases)
navires[5]=2  #Torpilleur (2 cases)
 
totalnavires=5  #Nombre total de bateaux
 
tir_colonne=""
tir_ligne=""