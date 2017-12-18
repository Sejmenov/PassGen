'''
Created on 10 Dec 2017

@author: sejmenov
'''
# added error handling!

import random

while True:
    try:
        n = int(input("How many characters should your password have?:"))
    except ValueError:
        print("Value must be a full number!")
        continue
    if n <= 6:
        print("Must be at least 7 characters long!")
        continue
    else:
        break
        
def passgen():
    password = ""
    for i in range(n):
        password = password + chr(random.randint(33, 127))
    return password

while True:
    try:
        m = int(input("How many passwords do you want to create?:"))
    except ValueError:
        print("Value must be a full number!")
        continue
    if m < 1:
        print("Must be atleast 1 password!")
        continue
    else:
        break
try:        
    file = open("Password.txt", "w")
    for i in range(m):
        print(i+1," ",passgen(),file=file)
        i +=1
finally:
    file.close()
