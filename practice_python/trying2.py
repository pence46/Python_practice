#http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
from datetime import date
year = date.today().year
name= input('your name:')
age= input('your age:')
'''  how to provide a safety net'''
try:
    val = int(age)
    agetohundred=str(year+100-int(age))
    x=int(input('How many times to repeat?'))
    for i in range(0,x):
        print(name + ', you will be 100 years old in '+agetohundred+ ' years.'+ '\n' )
except ValueError:
   print("That's not an int!")