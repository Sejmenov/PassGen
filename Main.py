'''
Created on 9 Dec 2017

@author: sejmenov
'''

import random

def passgen():
    password = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for i in range(20):
        password[i] = chr(random.randint(33, 127))
        i += 1
    return ''.join(password)

n = int(input("How many 20 symbols long passwords do you want to create?:"))
file = open("Password.txt", "w+")
for i in range(n):
    print(i+1," ",passgen(),file=file)
    i +=1
file.close()
