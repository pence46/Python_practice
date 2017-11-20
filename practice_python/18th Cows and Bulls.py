#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 7
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess,
# tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over.
#  Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
import random
while True:
    numberlist5=[int(i) for i in str(random.randint(10000,99999))]
    numberlist=numberlist5[1:5]
    bc=set(numberlist)
    bc=list(bc)
    if numberlist == bc:
        break
times=1
while True:
    guess=input('What is your guess(4 digit number)?\n')
    if guess == 'cheat':
        print(numberlist)
        print('Liar')
        break
    list_of_guess=[int(i) for i in str(guess)]  # a great way to split integers
    c,b=0,0

    for k in range(4):
        if list_of_guess[k] == numberlist[k]:
            c += 1
        elif list_of_guess[k] in numberlist:
            b += 1
    if numberlist == list_of_guess:
        print('Congrats, you won! You guessed in {} times.'.format(times))
        break

    else:
        print('{} bull(s) and {} cow(s). Try again.'.format(b, c))
        times += 1








