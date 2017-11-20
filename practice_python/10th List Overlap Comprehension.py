#Take two lists and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.
# Write this in one line of Python using at least one list comprehension.

#Randomly generate two lists to test this
# experimentation with the time() function and timeout in a loop
import random
import time
timeout= time.time() + 30
print(time.gmtime(1464573053))

d=[] # this line is added just to make 'while' work.
while len(d)<=5:              #I added while just to experiment with the process, it is not necessary
    a1=random.randint(1,25)
    b1=random.randint(1,25)
    a=random.sample(range(1000),a1)
    b=random.sample(range(1000),b1)
    c= [x for x in a for y in b if x==y]
    d=[]
    e=[d.append(i) for i in c if i  not in d ]
    if time.time() >= timeout:
        print('timeout')
        break
print(d)





'''
# solution for the original task
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c= [x for x in a for y in b if x==y]
d=[]
e=[d.append(i) for i in c if i  not in d ]
print(d)

#first take
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
shared_list=[]
print(len(shared_list))
for x in range(len(a)):
    for y in range(len(b)):
        if a[x] == b[y]:
            if a[x] not in shared_list:
                shared_list.append(a[x])

print(shared_list)
'''