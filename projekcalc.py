import operator
import random
import time
from unicodedata import name, numeric


score = 0
operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/', operator.truediv)]
print ("SELAMAT DATANG\nPERMAINAN KALKULATOR \n")
name = input ("Sila masukkan nama anda  : \n")
print("Anda dikehendaki menjawab 10 soalan yang diberi secara random\n")

for i in range(5):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op, fn = random.choice(operators)
    prompt = "What is {} {} {}?\n".format(a, op, b)
    if float(input(prompt)) == fn(a, b):
        score += 1
        print("You are correct")
    else:
        print("incorrect")


print("Nama anda ialah",name)
print("Terima Kasih kerana menjawab!\nSCORE ANDA ialah : {}".format(score))
    
