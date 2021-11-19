# adds libraries
import random

# variables
cal = " x 10?"

# generates an easy question
def easyQ():
    a1 = random.randint(0, 10) # generates random number between the two numbers in brackets
    da1 = a1 / 10
    print(f"What is {str(da1)}{cal}")
    givenanswer = input()
    if givenanswer == str(a1):
        print("Correct! Onto the next one!")
    else:
        print("Incorrect.")
        print(f"Correct Answer: {str(a1)}")

# generates a medium difficulty question
def mediumQ():
    a1 = random.randint(0, 15) # generates random number between the two numbers in brackets
    da1 = a1 / 10
    print(f"What is {str(da1)}{cal}")
    givenanswer = input()
    if givenanswer == str(a1):
        print("Correct! Onto the next one!")
    else:
        print("Incorrect.")
        print(f"Correct Answer: {str(a1)}")

# generates a hard difficulty question
def hardQ():
    a1 = random.randint(0, 25) # generates random number between the two numbers in brackets
    da1 = a1 / 10
    print(f"What is {str(da1)}{cal}")
    givenanswer = input()
    if givenanswer == str(a1):
        print("Correct! Onto the next one!")
    else:
        print("Incorrect.")
        print(f"Correct Answer: {str(a1)}")

# generates a difficult question
def difficultQ():
    a1 = random.randint(0, 30) # generates random number between the two numbers in brackets
    da1 = a1 / 10
    print(f"What is {str(da1)}{cal}")
    givenanswer = input()
    if givenanswer == str(a1):
        print("Correct! Onto the next one!")
    else:
        print("Incorrect.")
        print(f"Correct Answer: {str(a1)}")

easyQ()
mediumQ()
hardQ()
difficultQ()
print("If you failed a question, more practice would be beneficial.")
input()
