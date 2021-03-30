import random
import pyautogui

chars = "abcdefghijklmnopqrstuvwxyz0123456789"
charsList = list(chars)

password = pyautogui.password("Please enter the password: ")

guessPassword = ""

while (guessPassword != password):
    guessPassword = random.choices(charsList, k=len(password))

    print("["+ str(guessPassword)+ "]")

    if guessPassword == password:
        print("The password is: "+ "".join(guessPassword))
        break