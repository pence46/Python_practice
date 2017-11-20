#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.

#Second try, with function
number = int(input("How many Fibonacci numbers would you like to get generated ?"))
a= [1,1]

def addfibnumber():
    return a.append(a[i] + a[i+1])

for i in range(number-2):
    addfibnumber()

print(a)





''' first try
try:
    length=int(input('How long do you want the Fibonacci series to be?'))-2
    i=0
    fibo=[1,1]
    for i in range(0,length):
        a=int(fibo[i]+fibo[i+1])
        fibo.append(a)
    print(fibo)
except ValueError:
    print('Please input a number!')'''