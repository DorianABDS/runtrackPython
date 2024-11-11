import string
import random
from tkinter import *
# import customtkinter

def generate_password():
    # Mot de passe généré automatiquement entre 8 et 12 caractères
    password_length = random.randint(8,12)
    # Ensemble de tous les caractères pouvant se trouver dans le mot de passe
    password_chars = string.ascii_letters + string.punctuation + string.digits
    # Le mot de passe est généré aléatoirement
    password = "".join(random.choices(password_chars, k=password_length))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# créer une première fenêtre
window = Tk()

# personnaliser la fenêtre
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.minsize(300, 300)
window.iconbitmap("img/icon-password.ico")
window.config(background='#2D2D2D')

# créer la frame 
frame = Frame(window, bg='#2D2D2D')

#ajouter la frame
frame.pack(expand=YES)

# creation d'image
width = 300
height = 300
image = PhotoImage(file="img/password.png").zoom(20).subsample(40)
canvas = Canvas(frame, width=width, height=height, bg='#2D2D2D', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# creer une sous frame
right_frame = Frame(frame, bg='#2D2D2D')

# ajouter un premier texte
label_title = Label (right_frame, text="Bienvenue sur l'application", font=("Montserrat, 20"), bg='#2D2D2D', fg="white")
label_title.pack()

# # ajouter un input
password_entry = Entry(right_frame, font=("Montserrat, 15"), bg='#2D2D2D', fg="white")
password_entry.pack(fill=X)

# ajouter un premier boutton
generate_password_button = Button(right_frame, text="Générer un mot de passe", font=("Montserrat, 15"), bg='white', fg="#2D2D2D", command=generate_password)
generate_password_button.pack(pady=25, fill=X)

# on place la sous boite à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

# créer une nav
menu_bar = Menu(window)

# créer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# afficher la fenêtre
window.mainloop()