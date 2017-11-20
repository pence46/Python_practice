list=[1,1,2,3,5,8,13,21,34,55,89]
b=[]
try:
    numb= int(input('Number is :'))
    print([i for i in list if i<numb])
except ValueError:
    print('Not a number')




''' first code I wrote with multiple lines
for i in list:
    if i<numb:
        b.append(i)
print(b)'''
#    print([i for i in list if i<numb]) #one liner