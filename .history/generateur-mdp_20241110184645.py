import random

password_length = range(8,25)
password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{};':\",.<>/?\\|"
password = "".join(random.choices(password_chars, k=password_length))
fed = "Choisis le nombre de caractère que tu souhaites pour ton mot de passe : "

print("Ton nouveau mot de passe est :",password)
print("Enregistre le bien !")

while fed != password_length:
    print(int(input("Choisis le nombre de caractère que tu souhaites pour ton mot de passe : ")))
    if fed < password_length:
        print("Votre mot de passe est trop court")
    elif fed > password_length:
        print("Votre mot de passe est trop grand")
    else:
        fed == password_length
        print("Votre mot de passe est bon")