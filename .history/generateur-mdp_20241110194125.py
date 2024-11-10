import random
import tkinter import *
import customtkinter

password_length = random.randint(8,25)
password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{};':\",.<>/?\\|"
password = "".join(random.choices(password_chars, k=password_length))

print("Ton nouveau mot de passe est :",password)
print("Enregistre le bien !")

class window(tk):
    def __init__(self):
        super().__init__()
        self.title("Générateur de mot de passe")
        self.geometry("600x450")
        self.configure(bg="#E9E6E6")
        self.frame = customtkinter.CTkFrame(self,
                                            width=250,
                                            height=250,
                                            corner_radius=10)
        self.