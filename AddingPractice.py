# imports some libraries
import random
import time

# some variables
op = " + "
ansp = "Answer:"
qdifficulties = ["Easy: ","Medium: ","Hard: ","Difficult: "]

# generates an easy question
def easyQ():
    a1 = random.randint(0, 10) # generates random number between the two numbers in brackets
    a2 = random.randint(0, 10) # generates random number between the two numbers in brackets
    fin1 = str(a1)
    fin2 = str(a2)
    print(qdifficulties[0] + fin1 + op + fin2)
    time.sleep(5)
    print(ansp)
    print(a1 + a2)

# generates a medium difficulty question
def mediumQ():
    a1 = random.randint(5, 15) # generates random number between the two numbers in brackets
    a2 = random.randint(5, 15) # generates random number between the two numbers in brackets
    fin1 = str(a1)
    fin2 = str(a2)
    print(qdifficulties[1] + fin1 + op + fin2)
    time.sleep(6)
    print(ansp)
    print(a1 + a2)

def hardQ():
    a1 = random.randint(10, 20) # generates random number between the two numbers in brackets
    a2 = random.randint(10, 20) # generates random number between the two numbers in brackets
    fin1 = str(a1)
    fin2 = str(a2)
    print(qdifficulties[2] + fin1 + op + fin2)
    time.sleep(7)
    print(ansp)
    print(a1 + a2)

def difficultQ():
    a1 = random.randint(15, 25) # generates random number between the two numbers in brackets
    a2 = random.randint(15, 25) # generates random number between the two numbers in brackets
    fin1 = str(a1)
    fin2 = str(a2)
    print(qdifficulties[3] + fin1 + op + fin2)
    time.sleep(8)
    print(ansp)
    print(a1 + a2)

easyQ()
mediumQ()
hardQ()
difficultQ()
print("Here are the answers! If you failed a question, more practice would be beneficial.")
input()
