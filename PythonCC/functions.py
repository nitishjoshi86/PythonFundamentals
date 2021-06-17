#function is a block of code which only runs when it is called, we don't use curly brackets, we use indentation with tabs or spaces

#lambda function is a small anonymous function
#it can take any number of arguments, but can only have one expression

def sayhello(name):
    print(f'hello {name}')

sayhello('john cena')

def sayhello(name='sam'):
    print(f'hello {name}')

sayhello()

def getsum(num1,num2):
    total = num1+num2
    return total

#lambda

getsum = lambda num1,num2:num1+num2
print(getsum(10,9))