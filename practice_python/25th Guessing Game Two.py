#In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
#This time, we’re going to do exactly the opposite. You, the user, will have in your head a number
# between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high,
# too low, or your number.At the end of this exchange, your program should print out how many guesses it took to get your number.
#As the writer of this program, you will have to choose how your program will strategically guess.
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
#  But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range),
# and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy!
#  (We’ll talk about what is the optimal one next week with the solution.)
initial_guess=500
print('My guess is {}.'.format(initial_guess))
response=input('Is my guess right, low or high?\n')
wrong_answers=[0]
while True:
    wrong_answers.append(initial_guess)
    i = len(wrong_answers)-1
    if response == 'high':
        initial_guess = (wrong_answers[i]-(abs(wrong_answers[i]-wrong_answers[i-1])/2))
        print('My guess is {}.'.format(round(initial_guess)))
    elif response == 'low':
        initial_guess = (wrong_answers[i]+(abs(wrong_answers[i]-wrong_answers[i-1])/2))
        print('My guess is {}.'.format(round(initial_guess)))
    elif response=='right':
        break
    response=input('Is my guess right, low or high?\n')
print("Your number was {}. It took me {} time(s) to guess it right.".format(round(initial_guess), len(wrong_answers)-1))





'''initial_guess=50
print('My guess is {}.'.format(initial_guess))
response=input('Is my guess right, low or high?\n')
count=0
while True:
    count+=1
    if response=='high':
        initial_guess = round(initial_guess/2)
        print('My guess is {}.'.format(initial_guess))
        response=input('Is my guess right, low or high?\n')
    elif response=='low':
        if initial_guess>50:
            initial_guess = round(initial_guess+(100-initial_guess)/2)
            print('My guess is {}.'.format(initial_guess))
            response=input('Is my guess right, low or high?\n')
        elif initial_guess<50:
            initial_guess = round(initial_guess+(50-initial_guess)/2)
            print('My guess is {}.'.format(initial_guess))
            response=input('Is my guess right, low or high?\n')
    elif response=='right':
        break
    else:
        print('Please input a legit answer!')
print("I won. Your number was {}. It took me {} tries to guess it right.".format(initial_guess, count))
'''