# imports some libraries
import random
import time

# some variables
op = " ÷ "
ansp = "Answer:"
qdifficulties = ["Easy: ","Medium: ","Hard: ","Difficult: "]

# generates an easy question
def easyQ():
    a1 = random.randint(35, 60) # generates random number between the two numbers in brackets
    a2 = random.randint(15, 20) # generates random number between the two numbers in brackets
    fin1 = str(a1)
    fin2 = str(a2)
    print(qdifficulties[0] + fin1 + op + fin2)
    givenanswer = input()
    print(ansp)
    ans = a1 // a2
    print(a1 // a2)
    if givenanswer == str(ans):
        print("Correct.")
    else:
        print("Incorrect.")

# generates a medium difficulty question
def mediumQ():
    a1 = random.randint(45, 70) # generates random number between the two numbers in brackets
    a2 = random.randint(20, 25) # generates random number between the two numbers in brackets
    fin1 = str(a1)
    fin2 = str(a2)
    print(qdifficulties[1] + fin1 + op + fin2)
    givenanswer = input()
    print(ansp)
    ans = a1 // a2
    print(a1 // a2)
    if givenanswer == str(ans):
        print("Correct.")
    else:
        print("Incorrect.")

# generates a hard difficulty question
def hardQ():
    a1 = random.randint(55, 80) # generates random number between the two numbers in brackets
    a2 = random.randint(25, 30) # generates random number between the two numbers in brackets
    fin1 = str(a1)
    fin2 = str(a2)
    print(qdifficulties[2] + fin1 + op + fin2)
    givenanswer = input()
    print(ansp)
    ans = a1 // a2
    print(a1 // a2)
    if givenanswer == str(ans):
        print("Correct.")
    else:
        print("Incorrect.")

# generates a difficult question
def difficultQ():
    a1 = random.randint(65, 90) # generates random number between the two numbers in brackets
    a2 = random.randint(30, 35) # generates random number between the two numbers in brackets
    fin1 = str(a1)
    fin2 = str(a2)
    print(qdifficulties[3] + fin1 + op + fin2)
    givenanswer = input()
    print(ansp)
    ans = a1 // a2
    print(a1 // a2)
    if givenanswer == str(ans):
        print("Correct.")
    else:
        print("Incorrect.")

easyQ()
mediumQ()
hardQ()
difficultQ()
print("Here are the answers! If you failed a question, more practice would be beneficial.")
input()
