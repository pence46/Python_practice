#Write a password generator in Python. Be creative with how you generate passwords - strong passwords
# have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

def psw_generator(x):
    import random
    import string

    length_password= random.randint(x,x+5)
    password= "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length_password))
    print('Your password is '+password)

def psw_checker():  #check whether password is strong enough


    print('a')

pref=input('How strong do you want your password to be? \nweak or strong?')

if pref=='weak':
    psw_generator(10)
elif pref=='strong':
    psw_generator(20)





''' pro solution
length=random.randint(10,20)
finalpass="".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

print(finalpass)'''
''' pro solution -not mine

import random
import string

length=random.randint(10,20)
finalpass=''.join(random.choice(string.ascii_letters +  string.digits) for _ in range(length) )



print(finalpass)
'''

'''
class password:
    def method(self):
'''


