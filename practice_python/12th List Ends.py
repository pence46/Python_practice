#Write a program that takes a list of numbers (for example,
# a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.


#w/ list comprehension

a = [5, 10, 15, 20, 25]
def first_and_last(x):
    b=[z for z in x if z==x[0] or z== x[len(x)-1] ]

    print(b)
print(first_and_last(a))



'''
normal
a = [5, 10, 15, 20, 25]

def first_and_last(x):
    b=[]
    b.append(x[0])
    b.append(x[len(x)-1])
    print(b)
print(first_and_last(a))
'''