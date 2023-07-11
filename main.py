
from SRC.QUESTION_AND_ANSWERS import first_question, second_question

import random

name = input("Welcome to the game Who wants to be a millionare. What is your name? : ")

answer0=input("Are you ready to start the game "+name + "?")

if answer0 == "yes" or answer0 == "Yes":
    print ("Okay "+name+" there is first question : ")
else:
    print ("If you are not ready for the game so i must say goodbye")
    exit()

first_question_random = random.choice(first_question)
print(first_question_random)

answer1=input("What is your first answer? Please write the full answer exactly! ")

if answer1== "8" or answer1== "Prague" or answer1== "Clothes and sport accessories" or answer1== "South America" or answer1== "Dog":
    print("Perfect! This is the right answer")
else:
    print("Oh, this is the wrong answer. Please leave hot seat. Have a nice day")
    exit()

second_question_random = random.choice(second_question)
print(second_question_random)

answer2 = input("So there is a second question "+ name+ "What is your answer?")

if answer2== "Sony" or answer2== "Avocado spread" or answer2== "God of sea":
    print("You are clever. Is the right answer again")
else:
    print("I am sorry but this is wrong answer. Goodbye!")

#next questions and answers will be fill later





