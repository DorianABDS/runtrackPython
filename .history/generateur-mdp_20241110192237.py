from random import choice, randint

alphabet_min = [ chr(i) for i in range(97,123) ]
alphabet_maj = [ chr(i) for i in range(65,91) ]
chiffres = [ chr(i) for i in range(48,58) ]
caracteres_speciaux = [ '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@']

def pwd(n , min = True, maj = True, chif = True, cs = True):
    alphabets = dict()
    key = 0
    if min:
        alphabets[key] = alphabet_min
        key += 1
    if maj:
        alphabets[key] = alphabet_maj
        key += 1
    if chif:
        alphabets[key] = chiffres
        key += 1
    if cs:
        alphabets[key] = caracteres_speciaux
        key += 1
    
    mdp = ''
    for i in range(n):
            s = randint(0,key-1)
            mdp += choice( alphabets[s] )
            
    return mdp