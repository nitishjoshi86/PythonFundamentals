""" #ifelse conditions for true and false
#comparison operators(==,!=,>,<,>=,<=,)
#logical operators (and,or,not)
#membership operators (not, not in)



if x > y:
    print(f'{x} greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} lesser than {y}')

if x>2 and x<= 10:
        print(f'{x} is greater than 2 but less than or equal to 10')
if x>2 or x<= 10:
        print(f'{x} is greater than 2 but less than or equal to 10')
if not (x == 9):
        print(f'{x} is greater than 2 but less than or equal to 10')

 """
x = 13
y = 13
numbers = [1,2,3,4,5]
if x in numbers:
    print(x in numbers)

if x not in numbers:
    print(x not in numbers)
if x is y:
    print(x is y)

if x is not y:
    print(x is not y)