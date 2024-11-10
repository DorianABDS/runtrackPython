import random

password = "Choisis le nombre de caractère que tu souhaites pour ton mot de passe : "
password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{};':\",.<>/?\\|"
password_length = len(password)
password_gen = "".join(random.choices(password_chars, k=password_length))

print(password_length)
print("Ton nouveau mot de passe est :",password)
print("Enregistre le bien !")


print(int(input("Choisis le nombre de caractère que tu souhaites pour ton mot de passe : ")))
if password < password_length:
    print("Votre mot de passe est trop court")
elif password > password_length:
    print("Votre mot de passe est trop grand")
else:
    password == password_length
    print("Votre mot de passe est bon")