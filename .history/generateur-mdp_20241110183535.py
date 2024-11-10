import random

password_length = 8
password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{};':\",.<>/?\\|"
password = "".join(random.choices(password_chars, k=password_length))

print(input("Choisis le nombre de caractère que tu souhaites pour ton mot de passe : "))

print("Ton nouveau mot de passe est :",password)
print("Enregistre le bien !")