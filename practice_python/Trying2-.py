
try:
    numb= int(input('Input a number:\n'))
    check= int(input('Input a divisor:\n'))
    if numb%4==0:
        print('Even and multipe of 4')
    if numb%check==0:
        print('OK')
    else:
        print('Not OK')
except ValueError:
    print('It is not a number!')
except ZeroDivisionError:
    print('Divisor cannot be zero!')