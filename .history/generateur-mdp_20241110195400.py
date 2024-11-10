import random
import tkinter 
import customtkinter

password_length = random.randint(8,25)
password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{};':\",.<>/?\\|"
password = "".join(random.choices(password_chars, k=password_length))

print("Ton nouveau mot de passe est :",password)
print("Enregistre le bien !")

class Window(tkinter) :
    def __init__(self):
        super().__init__()
        self.title("Authenticator")
        self.geometry("600x450")
        self.configure(bg="#E9E6E6")
        self.frame = customtkinter.CTkFrame(self,
                                    width=250,
                                    height=258, 
                                    corner_radius=10)
        self.frame.place (relx=0.5, rely=0.5, anchor=CENTER)

        self.label = customtkinter.CTkLabel (self,text="Veuillez remplir le formulaire de connexion suivant : ",width=120, height=25, corner_radius=8, font=("Verdana", 19)) 
        self.label.place (relx=0.5, rely=0.1, anchor=CENTER)

        self.label2 = customtkinter.CTkLabel(self.frame, text="Identifiant :",width=120,height=25, corner_radius=8) 
        self.label2.place (relx=0.2, rely=0.1, anchor=CENTER)
        entry=customtkinter.CTkEntry(self.frame, width=120, height=25, corner_radius=10)
        entry.place(relx=0.7, rely=0.1, anchor=CENTER)

        self.label3 = customtkinter.CTkLabel(self.frame, text="Email : ",width=120,height=25, corner_radius=8) 
        self.label3.place (relx=0.2, rely=0.3, anchor=CENTER)
        entry2 = customtkinter.CTkEntry (self.frame, width=120,height=25, corner_radius=10) 
        entry2.place(relx=0.7, rely=0.3, anchor=CENTER)
        
        self.label4=customtkinter.CTkLabel(self.frame,text="Code : ", width=120, height=25, corner_radius=8)
        self.label4.place (relx=0.2, rely=0.5, anchor=CENTER)
        entry3 = customtkinter.CTkEntry(self.frame, width=120,height=25, corner_radius=10) 
        entry3.place(relx=0.7, rely=0.5, anchor=CENTER)

        self.label4 = customtkinter.CTkLabel(self.frame, text="Votre age:", width=120, height=25, corner_radius=8) 
        self.label4.place (relx=0.2, rely=0.7, anchor=CENTER)
        self.slider= customtkinter.CTkSlider (self.frame, width=120, height=16, border_width=5.5, command=self.slider_event)
        self.slider.place (relx=0.7, rely=0.7, anchor=CENTER)

        self.button = customtkinter.CTkButton(self.frame, text="Connexion", command=self.page2, width=200,height=32, border_width=0, corner_radius=8) 
        self.button.place(relx=0.5. rely-0.9, anchor=CENTER)