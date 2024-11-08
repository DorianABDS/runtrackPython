def main():
    # récolter une premiere note
    note1 = int(input("Entrer la premiere note"))
    # récolter une seconde note
    note2 = int(input("Entrer la seconde note"))
    # récolter une derniere note
    note3 = int(input("Entrer la derniere note"))
    # calculer la moyennne
    result = (note1 + note2 + note3) / 3
    # afficher le resultat
    print("la moyenne de l'élève est de " + str(result))



if __name__ == "__main__":
    main()
