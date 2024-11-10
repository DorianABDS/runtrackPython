# -*- coding: utf-8 -*-


import random


COLONNES = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}

LETTRES = ['A','B','C','D','E','F','G','H','I','J']

NAVIRES = {'Porte-avion':5,'Croiseur':4,'Contre-torpilleur1':3, 'Contre-torpilleur2':3, 'Sous-marin':2}

SENS = ['H','V']


IA_PORTE_AVION = []
IA_TIR_PORTE_AVION = []
IA_CROISEUR = []
IA_TIR_CROISEUR = []
IA_CONTRE_TORPILLEUR1 = []
IA_TIR_CONTRE_TORPILLEUR1 = []
IA_CONTRE_TORPILLEUR2 = []
IA_TIR_CONTRE_TORPILLEUR2 = []
IA_SOUS_MARIN = []
IA_TIR_SOUS_MARIN = []


PLAYER_PORTE_AVION = []
PLAYER_TIR_PORTE_AVION = []
PLAYER_CROISEUR = []
PLAYER_TIR_CROISEUR = []
PLAYER_CONTRE_TORPILLEUR1 = []
PLAYER_TIR_CONTRE_TORPILLEUR1 = []
PLAYER_CONTRE_TORPILLEUR2 = []
PLAYER_TIR_CONTRE_TORPILLEUR2 = []
PLAYER_SOUS_MARIN = []
PLAYER_TIR_SOUS_MARIN = []


def init_grille(symbole):
	grille=[]
	for i in range(10):
		grille.append([])
		for j in range (10):
			grille[i].append(symbole)
	return grille


def Affichage_grille_tirs(tirs):
	lettrecolonne=0
	print("  ", end="")
	while lettrecolonne<=9:
		print(LETTRES[lettrecolonne], end=" ")
		lettrecolonne+=1
	print()
	numligne=1
	while numligne<=10:
		for ligne in tirs:
			print(numligne, end=" ")
			for element in ligne:
				if element==-1:
					print(".", end=" ")
				elif element==0:
					print("*", end=" ")
				elif element==1 or element==2:
					print("X", end=" ")
			print()
			numligne+=1
            
def Affichage_grille_bateau(bateaux):

	lettrecolonne=0
	print("  ", end="")
	while lettrecolonne<=9:
		print(LETTRES[lettrecolonne], end=" ")
		lettrecolonne+=1
	print()
	numligne=1
	while numligne<=10:
		for ligne in bateaux:
			print(numligne, end=" ")
			for element in ligne:
				if element==0:
					print(".", end=" ")
				elif element==1:
					print("O", end=" ")
				elif element=='tirmanqué':
					print("*", end=" ")
				elif element=='tirtouché':
					print("X", end=" ")
			print()
			numligne+=1
            
            
def Init_placement_bateaux(c, l, bateau, sens, grille, joueur):
    taille=NAVIRES[bateau]
    if sens == 1:
        if c+(taille-1)<10 and c<=(10-taille):
            c1=c
            for i in range (taille):
                grille[l][c1]=1
                Sauvegarde_placement(c1, l, bateau, joueur)
                c1+=1
            return grille
    elif sens == 2:
        if l+(taille-1)<10 and l<=(10-taille):
            l1 = l
            for i in range(taille):
                grille[l1][c]=1
                Sauvegarde_placement(c, l1, bateau, joueur)
                l1+=1
            return grille
    else:
        print("/!\ Sens inconnu /!\ ")
        
        
def Placement_bateau_player(bateaux):

	for bateau in NAVIRES :
		taille=NAVIRES[bateau]
		print("\nVous allez placer le bateau :", bateau, "de longueur", taille, "case.\n")
		Affichage_grille_bateau(bateaux)
		possible = 0
		while possible != 1:
			x=str(input("\nEntrez ici la lettre souhaitée :"))
			x=x.upper()
			while x not in LETTRES:
				print("/!\ Erreur de lettre, veuillez resaisir la lettre ! /!\ ")
				x=str(input("Entrez ici la lettre souhaitée :"))
				x=x.upper()
			x=int(COLONNES[x])

			cond=0
			while cond!=1:	
				y = input("Entrez ici la colonne souhaitée :")
				while not y.isdigit():
					print("/!\ Erreur de colonne, veuillez resaisir la colonne ! /!\ ")
					y = input("Entrez ici la colonne souhaitée :")
				y=int(y)
				if y in range(1,11):
					y=y-1
					cond=1
				else:
					print("/!\ Erreur de colonne, resaisie ta colonne ! /!\ ")

			sens=str(input("Entrez ici le sens souhaité (Horizontal ou Vertical) [H/V] :"))
			sens=sens.upper()
			while sens not in SENS:
				print("/!\ Erreur de sens, veuillez resaisir le sens ! /!\ ")
				sens=str(input("Entrez ici le sens souhaité (Horizontal ou Vertical) [H/V] :"))
				sens=sens.upper()
			if sens=='H':
				sens=1
			elif sens=="V":
				sens=2

			possible = Placement_possible(x, y, taille, sens, bateaux)
			if possible == 0:
				print("Erreur dans le placement, recommencez votre placement !")
		Init_placement_bateaux(x, y, bateau, sens, bateaux, 'player')
	return bateaux


def Placement_bateaux_aleatoire(grille):

	for bateau in NAVIRES:
		taille = NAVIRES[bateau]
		possible = 0
		while possible != 1:
			x = random.randint(0,9)
			y = random.randint(0,9)
			sens = random.randint(1,2)
			possible = Placement_possible(x, y, taille, sens, grille)
		Init_placement_bateaux(x, y, bateau, sens, grille, "ia")
	return grille
            


def Placement_possible(c, l, taille, sens, grille):

	if sens == 1:
		if c+(taille-1)<10 and c<=(10-taille):
			c1 = c
			cpt = 0
			possible = 1
			while cpt !=taille and possible ==1:
				possible = 0
				if grille[l][c1] == 0:
					possible = 1
					c1+=1
					cpt+=1
			return possible
		else:
			return 0

	if sens == 2:
		if l+(taille-1)<10 and l<=(10-taille):
			l1 = l
			cpt = 0
			possible = 1
			while cpt !=taille and possible ==1:
				possible = 0
				if grille[l1][l] == 0:
					possible = 1
					l1+=1
					cpt+=1
			return possible
		else:
			return 0
        
def Sauvegarde_placement(x, y, bateau, joueur):
    
    if joueur == "ia":
        if bateau == "Porte-avion":
            IA_PORTE_AVION.append((x,y))
        elif bateau == "Croiseur":
            IA_CROISEUR.append((x,y))
        elif bateau == "Contre-torpilleur1":
            IA_CONTRE_TORPILLEUR1.append((x,y))
        elif bateau == "Contre-torpilleur2":
            IA_CONTRE_TORPILLEUR2.append((x,y))
        elif bateau == "Sous-marin":
            IA_SOUS_MARIN.append((x,y))
            
    elif joueur == 'player':
        if bateau == "Porte-avion":
            PLAYER_PORTE_AVION.append((x,y))
        elif bateau == "Croiseur":
            PLAYER_CROISEUR.append((x,y))
        elif bateau == "Contre-torpilleur1":
            PLAYER_CONTRE_TORPILLEUR1.append((x,y))
        elif bateau == "Contre-torpilleur2":
            PLAYER_CONTRE_TORPILLEUR2.append((x,y))
        elif bateau == "Sous-marin":
            PLAYER_SOUS_MARIN.append((x,y))
            
            
def Tour_de_jeu(tirs, joueur):

    if joueur=='player':
        print("Saisissez la position de votre prochain tir :")
        colonne=str(input("Lettre de la colonne :"))
        colonne=colonne.upper() #Répare l'erreur si l'utilisateur rentre un a au lieu de A
        while colonne not in LETTRES:
            print("/!\ Erreur de lettre, veuillez ressaisir votre lettre ! /!\ ")
            colonne=str(input("Lettre de la colonne :"))
            colonne=colonne.upper()
        colonne=int(COLONNES[colonne])
        
        cond=0
        while cond!=1:	
            ligne = input("N° de la ligne :")
            while not ligne.isdigit():
                print("/!\ Erreur de ligne, veuillez ressaisir votre ligne ! /!\ ")
                ligne = input("N° de la ligne :")
            ligne = int(ligne)
            if ligne in range(1,11):
                ligne = ligne-1 #car ligne 5 en vrai = ligne 4 en python
                cond=1
            else:
                print("/!\ Erreur de ligne, veuillez ressaisir votre ligne ! /!\ ")
                
    elif joueur == "ia":
        ligne = random.randint(0,9)
        colonne = random.randint(0,9)

    if (0<=ligne<=9) and (0<=colonne<=9) and (tirs[ligne][colonne]==-1):
        return (ligne, colonne)
    else:
        if joueur=='player':
            print("/!\ Erreur tir (déjà fait ou incorrect). Veuillez recommencer votre tir ! /!\ ")
        return Tour_de_jeu(tirs, joueur)
    
def tirer(bateaux, tirs, ligne, colonne, joueur):
    
    if joueur == "player":
        PORTE_AVION = IA_PORTE_AVION
        TIR_PORTE_AVION = IA_TIR_PORTE_AVION
        CROISEUR = IA_CROISEUR
        TIR_CROISEUR = IA_TIR_CROISEUR
        CONTRE_TORPILLEUR1 = IA_CONTRE_TORPILLEUR1
        TIR_CONTRE_TORPILLEUR1 = IA_TIR_CONTRE_TORPILLEUR1
        CONTRE_TORPILLEUR2 = IA_CONTRE_TORPILLEUR2
        TIR_CONTRE_TORPILLEUR2 = IA_TIR_CONTRE_TORPILLEUR2
        SOUS_MARIN = IA_SOUS_MARIN
        TIR_SOUS_MARIN = IA_TIR_SOUS_MARIN

        
    elif joueur == "ia":
        PORTE_AVION = PLAYER_PORTE_AVION
        TIR_PORTE_AVION = PLAYER_TIR_PORTE_AVION
        CROISEUR = PLAYER_CROISEUR
        TIR_CROISEUR = PLAYER_TIR_CROISEUR
        CONTRE_TORPILLEUR1 = PLAYER_CONTRE_TORPILLEUR1
        TIR_CONTRE_TORPILLEUR1 = PLAYER_TIR_CONTRE_TORPILLEUR1
        CONTRE_TORPILLEUR2 = PLAYER_CONTRE_TORPILLEUR2
        TIR_CONTRE_TORPILLEUR2 = PLAYER_TIR_CONTRE_TORPILLEUR2
        SOUS_MARIN = PLAYER_SOUS_MARIN
        TIR_SOUS_MARIN = PLAYER_TIR_SOUS_MARIN
    
    res=resultat_tir(bateaux, ligne, colonne, joueur)
    if res==0:
        tirs[ligne][colonne]=0
        return 0
    
    elif res==1:
        tirs[ligne][colonne]=1
        return 1
    
    elif res==2:
        tirs[ligne][colonne]=2
        return 2


def resultat_tir(bateaux, ligne, colonne, joueur):

    if joueur == "player":
        PORTE_AVION = IA_PORTE_AVION
        TIR_PORTE_AVION = IA_TIR_PORTE_AVION
        CROISEUR = IA_CROISEUR
        TIR_CROISEUR = IA_TIR_CROISEUR
        CONTRE_TORPILLEUR1 = IA_CONTRE_TORPILLEUR1
        TIR_CONTRE_TORPILLEUR1 = IA_TIR_CONTRE_TORPILLEUR1
        CONTRE_TORPILLEUR2 = IA_CONTRE_TORPILLEUR2
        TIR_CONTRE_TORPILLEUR2 = IA_TIR_CONTRE_TORPILLEUR2
        SOUS_MARIN = IA_SOUS_MARIN
        TIR_SOUS_MARIN = IA_TIR_SOUS_MARIN
    
    elif joueur == "ia":
        PORTE_AVION = PLAYER_PORTE_AVION
        TIR_PORTE_AVION = PLAYER_TIR_PORTE_AVION
        CROISEUR = PLAYER_CROISEUR
        TIR_CROISEUR = PLAYER_TIR_CROISEUR
        CONTRE_TORPILLEUR1 = PLAYER_CONTRE_TORPILLEUR1
        TIR_CONTRE_TORPILLEUR1 = PLAYER_TIR_CONTRE_TORPILLEUR1
        CONTRE_TORPILLEUR2 = PLAYER_CONTRE_TORPILLEUR2
        TIR_CONTRE_TORPILLEUR2 = PLAYER_TIR_CONTRE_TORPILLEUR2
        SOUS_MARIN = PLAYER_SOUS_MARIN
        TIR_SOUS_MARIN = PLAYER_TIR_SOUS_MARIN
    
    if (bateaux[ligne][colonne]==0):
        return 0
    
    elif (bateaux[ligne][colonne]==1):
        if ((ligne, colonne) in PORTE_AVION):
            PORTE_AVION.remove((ligne, colonne))
            TIR_PORTE_AVION.append((ligne, colonne))
            if len(PORTE_AVION)!=0:
                return 1
            elif len(PORTE_AVION)==0:
                return 2
        
        elif ((ligne, colonne) in CROISEUR):
            CROISEUR.remove((ligne, colonne))
            TIR_CROISEUR.append((ligne, colonne))
            if len(CROISEUR)!=0:
                return 1
            elif len(CROISEUR)==0:
                return 2
        
        if ((ligne, colonne) in CONTRE_TORPILLEUR1):
            CONTRE_TORPILLEUR1.remove((ligne, colonne))
            TIR_CONTRE_TORPILLEUR1.append((ligne, colonne))
            if len(CONTRE_TORPILLEUR1)!=0:
                return 1
            elif len(CONTRE_TORPILLEUR1)==0:
                return 2
            
        elif ((ligne, colonne) in CONTRE_TORPILLEUR2):
            CONTRE_TORPILLEUR2.remove((ligne, colonne))
            TIR_CONTRE_TORPILLEUR2.append((ligne, colonne))
            if len(CONTRE_TORPILLEUR2)!=0:
                return 1
            elif len(CONTRE_TORPILLEUR2)==0:
                return 2
        
        elif ((ligne, colonne) in SOUS_MARIN):
            SOUS_MARIN.remove((ligne, colonne))
            TIR_SOUS_MARIN.append((ligne, colonne))
            if len(SOUS_MARIN)!=0:
                return 1
            elif len(SOUS_MARIN)==0:
                return 2
            

            
def partie_finie(tirs):

	#Cette partie va compter le nombre de 2 dans le tableau
	compteur=0
	for ligne in tirs:
		for valeur in ligne:
			if valeur==2:
				compteur +=1
	#Cette partie va compter la somme de la longueur de tous les bateaux
	total=0
	for valeur in NAVIRES.values():
		total += valeur
	if compteur==total:
		return True
	else:
		return False

    
def debut():
    
    print("            -------------------------------------")
    print("            - Bienvenue dans la Bataille Navale -")
    print("            -------------------------------------\n")
    print("\nVous allez affronter un ordinateur, les règles sont les suivantes:\n")
    print("- Vous pouvez disposer les bateAux de façon horizontale ou de façon verticale")
    print("- Attention? vous ne pouvez pas mettre deux bateaux l'un sur l'autre\n")
    print("\nVous disposez des bateaux suivants:")
    print("- 1 Porte-avion (5 cases)\n - 1 Croiseur (4 cases)\n - 2 Contre-torpilleurs (3 cases)\n - 1 Sous-marin (2 cases)\n \n")
    print("\nVous êtes maintenant prêt à jouer, bonne chance ! \n")
    
def fin(score_player, score_ia):
    print("Votre score final :", score_player)
    print("Score final de l'ordinateur :", score_ia)
    print("\n          -----------------------------------------  ")
    print("            - Vous avez gagné la partie, bien joué ! - ")
    print("            -----------------------------------------\n")


def Jeu():

    bateaux_player = init_grille(0)
    tirs_player = init_grille(-1)

    bateaux_ia = init_grille(0)
    bateaux_ia = Placement_bateaux_aleatoire(bateaux_ia)
    tirs_ia = init_grille(-1)
    
    score_player=25
    score_ia=25

    debut()

    print("Pour placer vos bateaux, saisissez la case de départ,\nensuite son sens. Il se placera automatiquement.\n")
    input("Appuyez sur <Entrée> pour commencer à placer vos bateaux.")

    Placement_bateau_player(bateaux_player)
    print()

    copie_bateaux_player=list(bateaux_player)

    input("Votre grille est prête, appuyez sur <Entrée> pour commencer à jouer !")
    while not partie_finie(tirs_player) and not partie_finie(tirs_ia):
        print("Vos bateaux (O) et les tirs de l'ordinateur :\n - (*) pour un tir manqué\n - (X) pour un bon tir\n")
        Affichage_grille_bateau(copie_bateaux_player)
        print("\nVotre grille de tirs :\n")
        Affichage_grille_tirs(tirs_player)
        print("\nVotre score :", score_player)
        print("\nScore ordinateur :", score_ia)
        print("\nA vous de jouer !\n")

        res_player=Tour_de_jeu(tirs_player, 'player')
        tir=tirer(bateaux_ia, tirs_player, res_player[0], res_player[1], 'player')
        if tir==0:
            print("\nVous avez raté votre tir.")
            score_player -= 1
        elif tir==1:
            print("\nVous avez touché un bateau.")
            score_player += 3
        elif tir==2:
            print("\nVous avez coulé un bateau.")
            score_player += 3
        
        #while tirer(bateaux_ia, tirs_player, res[0], res[1], 'player')==1 or tirer(bateaux_ia, tirs_player, res[0], res[1], 'player')==2:
         #   res=Tour_de_jeu(tirs_player, 'player')
          #  tirer(bateaux_ia, tirs_player, res[0], res[1], 'player')

        res_ordi=Tour_de_jeu(tirs_ia, 'ia')
        print("L'ordinateur à tiré en", LETTRES[res_ordi[1]], res_ordi[0]+1)
        res=tirer(bateaux_player, tirs_ia, res_ordi[0], res_ordi[1], 'ia')
        triche=input("\nRentrez 0 si l'ordinateur a manqué son tir, 1 si l'ordinateur a touché un bateau et 2 s'il a coulé un bateau :")
        triche=int(triche)
        while triche not in (0,1,2):
            print("\nVous n'avez pas choisi une valeur valide")
            triche=input("\nRentrez 0 si l'ordinateur a manqué son tir, 1 si l'ordinateur a touché un bateau et 2 s'il a coulé un bateau :")
            triche=int(triche)
            
        if res != triche:
            print("Vous avez triché, vous perdez 10 points.")
            score_player -= 10
        
        if res==0:
            print("\nL'ordinateur a raté son tir")
            score_ia -= 1
        if res==1:
            print("\nL'ordinateur à touché un bateau")
            score_ia += 3
        if res==2:
            print("\nL'ordinateur a coulé un bateau")
            score_ia += 3
            
        if res==0:
            copie_bateaux_player[res_ordi[0]][res_ordi[1]]='tirmanqué'
        else:
            copie_bateaux_player[res_ordi[0]][res_ordi[1]]='tirtouché'
#            while copie_bateaux_player[res_ordi[0]][res_ordi[1]]=='tirtouché':
#                res=tirer(bateaux_player, tirs_ia, res_ordi[0], res_ordi[1], 'ia')
#                if res==0:
#                    copie_bateaux_player[res_ordi[0]][res_ordi[1]]='tirmanqué'
#                else:
#                    copie_bateaux_player[res_ordi[0]][res_ordi[1]]='tirtouché'
        
		#Réponses affichées pour le test, à retirer apres !
        #Affichage_grille_bateau(bateaux_ia)
        
        print("Votre score :", score_player)
        print("Score de l'ordinateur :", score_ia)

        if partie_finie(tirs_player) or score_ia == 0:
            fin()
        elif partie_finie(tirs_ia) or score_player == 0:
            print("Votre score final :", score_player)
            print("Score final de l'ordinateur :", score_ia)
            print("\n          -----------------------------------------  ")
            print("            - L'ordinateur a gagné, dommage... -")
            print("            -----------------------------------------\n")
        else:
            input("Appuyez sur <Entrée> pour continuer...")
            
            
Jeu()