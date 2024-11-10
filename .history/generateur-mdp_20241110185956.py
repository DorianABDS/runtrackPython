import random

password = input("Choisis le nombre de caractère que tu souhaites pour ton mot de passe : ")
password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{};':\",.<>/?\\|"
password_length = len(password)
password_gen = "".join(random.choices(password_chars, k=password_length))


if password_length < 8:
    print("Votre mot de passe est trop court")
elif 8 < password_length <= 12:
    print("Votre mot de passe parfait")
else:
    password_length > 12:
    print("Votre mot de passe est trop grand")