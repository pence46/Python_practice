#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

#make it that user can type exit for the first question to exit the game
# and game ends when the user predicted the number
# also in the end user should know how many times he/she spent

import random

list=[]
while True:

    thenumber= random.randint(1,9)
    guess=input('What is your guess(between 1 and 9)?')
    list.append(guess)

    try:
        if guess=='exit': break
        else: guess=int(guess)
        if guess>thenumber:
                print('Too high '+str(thenumber))
        elif guess==thenumber:
                print('exactly right. The number was '+str(thenumber))
                break
        elif guess<thenumber:
                print('too low '+str(thenumber))

    except ValueError:
        print('Please input a legit number!')



print("You have guessed "+str(len(list))+" time(s).")
