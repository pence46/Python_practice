import random
#write a program that returns a list that contains only the elements that are common between
# the lists (without duplicates). Make sure your program works on two lists of different sizes.

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

'''
x=0
while x<=2:
    shared_members=[]
    a=random.sample(range(100),11)
    b=random.sample(range(100),13)
    lena=len(a)
    lenb=len(b)
    shared_members=[]
    for n in range(0,lenb):
        for i in range(0,lena):
                if a[i]==b[n]:
                    if a[i] not in shared_members:
                        shared_members.append(a[i])
    print(shared_members)
    x+=1
'''
#Go back and do Exercise 5 using sets, and write the solution for that in a different function.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def remove_duplicates(x, y):
    b=x+y
    b=set(b)
    b=list(b)
    print(b)


remove_duplicates(a, c)


