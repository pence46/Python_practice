while True:
    numb=int(input('Write the number  you want to test: '))
    divisors=[]
    try:
            for i in range(1,numb+1):
                        if numb%i==0:
                            divisors.append(i)
            print(divisors if len(divisors)>2 else print('It is a prime number'))
    except ValueError:
        print('Not a number!')