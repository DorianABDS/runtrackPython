import random
ai_bateaux = [["A1", "A2", "A3"],
              ["B1"],
              ["C1", "C2"]]
 
usr_bateaux = [["A1", "A2", "A3"],
              ["C1"],
              ["B3", "C3"]]
 
grille_usr = [["?", "?", "?"],
              ["?", "?", "?"],
              ["?", "?", "?"]]

def affiche(grille):
    for ligne in grille:
        ligne_a_afficher='|'
        for pion in ligne:
            ligne_a_afficher+=pion+'|'
        print(ligne_a_afficher)
 
def essai_usr():
     
    inp = input("Quel casse souhaitez vous essayer ?")
 
    pos_x = 2
    pos_y = 0
 
#     if (grille_usr[pos_y][pos_x] != "?"):
#             print("Déja tenté bro")
#         essai_usr()
   
#     if (ai_bateaux contient inp):
#         ai_bateaux.remove(inp)
 
#         if (ai_bateaux contient [])
#             print("Touché coulé!")
#             ai_bateaux.remove([]) 
#         else
#             print("Touché")
 
#     essai_ai() 
 
# def essai_ai():
  
#     essai_usr() 
 
# turn = "Usr"
# isFinished = False
 
 
# while not isFinished:
 
#   while turn == "Usr":
#     if essai_usr():
#       turn == "AI"
   
#   essai_ai()
#   turn = "Usr"
