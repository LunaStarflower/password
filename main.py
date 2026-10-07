import random

password_length = int(input("Podaj długość hasła: "))

password_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]|;:,.<>?/~`"

password = ""

for i in range(password_length):
    password += random.choice(password_characters)

print("Wygenerowane hasło:", password)