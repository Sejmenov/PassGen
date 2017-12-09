'''
Created on 9 Dec 2017

@author: sejmenov
'''
import random

def random_symbol(let):
    abc = "qwertyuiopasdfghjklzxcvbnm"
    ABC = "QWERTYUIOPASDFGHJKLZXCVBNM"
    num = "0123456789"
    NUM = "!@#$*"
    a = random.randint(0,25)
    b = random.randint(0,25)
    c = random.randint(0,9)
    d = random.randint(0,4)
    if let == "a":
        return abc[a]
    elif let == "b":
        return ABC[b]
    elif let == "c":
        return num[c]
    else:
        return NUM[d]

def passgen():
    password = ["a","b","c","d","e","f","g","h","j","k"]
    for i in range(10):
        password[i]= random_symbol(random.choice("abcd"))
        i += 1
    return ''.join(password)

n = int(input("How many 10 letter passwords do you want to create?:"))
file = open("Password.txt", "w+")
for i in range(n):
    print(i+1," ",passgen(),file=file)
    i +=1
file.close()

