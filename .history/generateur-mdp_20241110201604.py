import random

# Mot de passe généré automatiquement entre 8 et 12 caractère
password_length = random.randint(8,12)
password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{};':\",.<>/?\\|"
password = "".join(random.choices(password_chars, k=password_length))

print("Ton nouveau mot de passe sera généré entre 8 et 12 caractère. Ni plus, ni moins ! ")
print("Ton nouveau mot de passe est :",password)
print("Il contient" ,password_length,"caractères... Enregistre le bien !")