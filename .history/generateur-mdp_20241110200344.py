import random

password_length = random.randint(8,12)
password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{};':\",.<>/?\\|"
password = "".join(random.choices(password_chars, k=password_length))

print("Ton nouveau mot de passe est :",__password__,"et contient" ,__password_length__,"caractères")
print("Enregistre le bien !")