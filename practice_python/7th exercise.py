#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([numb for numb in a if numb%2==0])




''' second try after looking it up in stackoverflow
b=[]
for i in range(len(a)): b.append(a[i]) if a[i]%2 ==0 else None; print(b)

'''


''' without one line of code
b=[]

i=0
for i in range(len(a)):
    if a[i]%2 ==0:
        b.append(a[i])
print(b)
'''