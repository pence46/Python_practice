#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
#r, s ,p

repeat='yes'
while repeat=='yes':
    p1=input('Player1 please input your choice:')
    p2=input('Player2 please input your choice:')
    if p1==p2:
        print('Draw!')
    elif p1=='r' and p2=='s':
        print('Player1 wins')
    elif p1=='r' and p2=='p':
        print('Player2 wins')
    elif p1=='s' and p2=='r':
        print('Player2 wins')
    elif p1=='s' and p2=='p':
        print('Player1 wins')
    elif p1=='p' and p2=='r':
        print('Player1 wins')
    elif p1=='p' and p2=='s':
        print('Player2 wins')
    repeat=input("Do you want to play again?('yes' or 'no')")
print('Thank you for playing.')

''' first try, could not get it to run again
p1=input('Player1 please input your choice:')
p2=input('Player2 please input your choice:')

if p1==p2:
    print('Draw!')
elif p1=='r' and p2=='s':
    print('Player1 wins')
elif p1=='r' and p2=='p':
        print('Player2 wins')
elif p1=='s' and p2=='r':
        print('Player2 wins')
elif p1=='s' and p2=='p':
        print('Player1 wins')
elif p1=='p' and p2=='r':
        print('Player1 wins')
elif p1=='p' and p2=='s':
        print('Player2 wins')
'''