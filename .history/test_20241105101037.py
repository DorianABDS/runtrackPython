def main():
    # récolter une premiere note
    note1 = input("Entrer la premiere note")
    # récolter une seconde note
    note2 = input("Entrer la seconde note")
    # récolter une derniere note
    note3 = input("Entrer la derniere note")
    # calculer la moyennne
    result = (note1 + note2 + note3) / 3
    # afficher le resultat
    print("le resultat est " + result)



if __name__ == "__main__":
    main()
