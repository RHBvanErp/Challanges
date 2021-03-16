import string
import random

length = int(input("Hoeveel tekens wil je in je wachtwoord? | "))
lowerCase = int(input("Hoeveel kleine letters wil je in je wachtwoord? | "))
upperCase = int(input("Hoeveel hoofdletters wil je in je wachtwoord? | "))
number = int(input("Hoeveel cijfers wil je in je wachtwoord? | "))

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.ascii_punctuation)

all = lower + upper + numbers + symbols

if length < 5:
    print("Minimaal 4 tekens, probeer opnieuw. ")
    length = int(input("Hoeveel tekens wil je in je wachtwoord? | "))
    lowerCase = int(input("Hoeveel kleine letters wil je in je wachtwoord? | "))
    upperCase = int(input("Hoeveel hoofdletters wil je in je wachtwoord? | "))
    number = int(input("Hoeveel cijfers wil je in je wachtwoord? | "))

else:
    low = []
    up = []
    num = []
    total = number + upperCase + lowerCase
    
    x = 0 
    while x <(length):
        if x < (lowerCase):
            lower.append(random.choice(lower))
            x += 1
            print (x, "low")
            if low == lowerCase:
                continue
        
        elif x < (upperCase + lowerCase):
            upper.append(random.choice(upper))
            x += 1
            print (x, "up")
            if up == upperCase:
                break
            
        elif x < (total):
            number.append(random.choice(numbers))
            x += 1
            print (x, "num")
            if num == number:
                continue
            
    password = "".join(random.sample(lower + upper + number))

    print(password) 
