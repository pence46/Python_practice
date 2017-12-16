#Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
try:  #try except is useless for this, I added anyhow.
    text=input('Write down the the text you want to be checked:\n')
    lentext=len(text)
    i=0

    for i in range(0,lentext-1):
        if not text[i] == text[lentext-1-i]:
            condition= False
            break
        else:
            condition=True
        i+=1
except ValueError:
    print('Not a string')

if condition:
    print('Palindir')
elif not condition:
    print('Not Palindir')
