def main():
    wallet = int(input("entrez votre solde: 75"))
    produit = 50

    solde = wallet - produit
    print("il vous reste", solde, "euros")

if __name__ == "__main__":
    main()
