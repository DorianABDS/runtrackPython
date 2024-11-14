import random, string
from tkinter import *
import customtkinter

# # créer une première fenêtre
# window = Tk()

# # personnaliser la fenêtre
# window.title("Générateur de mot de passe")
# window.geometry("800x500")
# window.minsize(780, 480)
# window.iconbitmap("img/icon-password.ico")
# window.config(background='#2D2D2D')

# # créer la frame 
# frame = Frame(window, bg='#2D2D2D')

# #ajouter la frame
# frame.pack(expand=YES)

# # creation d'image
# width = 300
# height = 300
# image = PhotoImage(file="img/password.png").zoom(20).subsample(40)
# canvas = Canvas(frame, width=width, height=height, bg='#2D2D2D', bd=0, highlightthickness=0)
# canvas.create_image(width/2, height/2, image=image)
# canvas.grid(row=0, column=0, sticky=W)

# # creer une sous frame
# right_frame = Frame(frame, bg='#2D2D2D')

# # titre
# title = Label(right_frame, text="Configurer votre mot de passe avant de le générer", font=("Montserrat, 15"), bg='#2D2D2D', fg="white")
# title.pack()

# def selection():
#     selection = choice.get()

# # créer des checkbox
# choice = IntVar()
# c1 = Radiobutton(right_frame, text="Minuscule et Majuscule", variable=choice, value=1, command=selection, font=("Montserrat, 15"), bg='#2D2D2D', fg="green")
# c1.pack()
# c2 = Radiobutton(right_frame, text="Chiffre", variable=choice, value=2, command=selection, font=("Montserrat, 15"), bg='#2D2D2D', fg="green")
# c2.pack()
# c3 = Radiobutton(right_frame, text="Spéciaux", variable=choice, value=3, command=selection, font=("Montserrat, 15"), bg='#2D2D2D', fg="green")
# c3.pack()

# # ajout d'un input variable
# lentitle = Label(right_frame, text="Longueur du mot de passe", font=("Montserrat, 15"), bg='#2D2D2D', fg="white")
# lentitle.pack()

# val = IntVar()
# spinlenght = Spinbox(right_frame, from_=8, to=15, textvariable=val, width=3)
# spinlenght.pack()

# # ajouter un premier boutton
# def callback():
#     lsum.config(text=passgen())

# passgen_button = Button(right_frame, text="Générer un mot de passe", font=("Montserrat, 15"), bg='white', fg="#2D2D2D", command=selection)
# passgen_button.pack(pady=10, fill=X)
# password = str(callback)

# # Input du mot de passe
# lsum = Entry(right_frame, text="")
# lsum.pack()

# # suggestion de modification du mot de passe
# min_maj = string.ascii_uppercase + string.ascii_lowercase
# chiffre = string.ascii_uppercase + string.ascii_lowercase + string.digits
# symbol = string.punctuation
# spéciaux = min_maj + chiffre + symbol

# def passgen():
#     if choice.get() == 1:
#         return"".join(random.password(min_maj, val.get()))
#     elif choice.get() == 2:
#         return"".join(random.password(chiffre, val.get()))
#     elif choice.get() == 3:
#         return"".join(random.password(spéciaux, val.get()))

# # on place la sous boite à droite de la frame principale
# right_frame.grid(row=0, column=1, sticky=W)

# # créer une nav
# menu_bar = Menu(window)

# # créer un premier menu
# file_menu = Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Nouveau", command=callback)
# file_menu.add_command(label="Quitter", command=window.quit)
# menu_bar.add_cascade(label="Fichier", menu=file_menu)

# # configurer notre fenêtre pour ajouter cette menu bar
# window.config(menu=menu_bar)

# # afficher la fenêtre
# window.mainloop()

min_maj = string.ascii_uppercase + string.ascii_lowercase
chiffre = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbol = string.punctuation
speciaux = min_maj + chiffre + symbol

while True:
    lenpassword = int(input("Entrez la longueur du mot de passe :"))
    nombrepsw = int(input("Entrez le nombre de mot de caractère à afficher : "))
    speciauxpsw = int(input("Ajouter des caractère spéciaux dans mon mot de passe"))
    if speciauxpsw == "oui":
        for i in range(0,nombrepsw):
            psw = ""
            for i in range(0,lenpassword):
                cpsw = random.choice(speciaux)
                psw = psw + cpsw
            print("Votre mot de passe est")
    elif speciauxpsw == "non":
        for i in range(0,nombrepsw):
            psw = ""
            for i in range(0,lenpassword):
                cpsw = random.choice(speciaux)
                psw = psw + cpsw
            print("Votre mot de passe est")
    else:
        speciauxpsw != "oui" or "non"
        print ("ERREUR")