import random
from tkinter import *
import customtkinter

# créer une première fenêtre
window = Tk()

# personnaliser la fenêtre
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.minsize(300, 300)
window.iconbitmap("img/generateur.mdp.ico")
window.config(background='#2D2D2D')

# creation d'image
width = 300
height = 300
image = PhotoImage(file="img/generateur.mdp.ico") .zoom(35).subsample(32)
canvas = Canvas(window)

# créer la frame 
frame = Frame(window, bg='#2D2D2D')

#ajouter la frame
frame.pack(expand=YES)

# ajouter un premier texte
label_title = Label (frame, text="Bienvenue sur l'application", font=("Montserrat, 20"), bg='#2D2D2D', fg="white")
label_title.pack()

# ajouter un second texte
label_subtitle = Label (frame, text="Hello world", font=("Montserrat, 15"), bg='#2D2D2D', fg="white")
label_subtitle.pack()

# ajouter un premier boutton
gen = Button(frame, text="Générer un mot de passe", font=("Montserrat, 15"), bg='white', fg="#2D2D2D")
gen.pack(pady=25, fill=X)

# afficher la fenêtre
window.mainloop()

# Mot de passe généré automatiquement entre 8 et 12 caractères
password_length = random.randint(8,12)
# Ensemble de tous les caractères pouvant se trouver dans le mot de passe
password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{};':\",.<>/?\\|"
# Le mot de passe est généré aléatoirement
password = "".join(random.choices(password_chars, k=password_length))

# texte de mise en page 
print("Le nouveau mot de passe sera généré entre 8 et 12 caractères. Ni plus, ni moins ! ")
print("--------------------------------------------------------------------------------------")
print("Le mot de passe est :",password)
print("Il contient" ,password_length,"caractères... Enregistre-le bien !")