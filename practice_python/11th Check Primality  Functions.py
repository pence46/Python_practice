#Ask the user for a number and determine whether the number is prime or not.

def primer(a):

    if a==2:
        print('{0} is a prime number.'.format(a))
    elif a<=1:
        print('{0} is not a prime number by definition.'.format(a))

    for i in range(2,a):
        if a%i==0:
            print('{0} is not a prime number. It is divisible by {1}'.format(a,i))
            break
        else:
            print('{0} is a prime number.'.format(a))
            break

try:
    primer(int(input('Please write the number you want to test!')))
except ValueError:
    print('Please input a valid number!')
