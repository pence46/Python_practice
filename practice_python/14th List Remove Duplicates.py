#Write a program (function!) that takes a list and returns a new list that contains
# all the elements of the first list minus all the duplicates.

a = [10, 15, 40, 30, 10, 15, 15]

def remove_duplicates(x):
    x=set(x)
    x=list(x)

    print(x)


remove_duplicates(a)



''' without set
a = [10, 15, 40, 30, 10, 15, 15]

def remove_duplicates(x):
    b=[]
    for a in x:
        for i in range(len(x)):
            if a not in b: b.append(a)
    print(b)

remove_duplicates(a)
'''
