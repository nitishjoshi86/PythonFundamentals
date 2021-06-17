#string formatting and method

from functions import getsum


name = 'nitish'
age = 37

#concatenate

print('hello, my name is ' + name + ' and i am '+str(age) +' years old')

#string formatting

#arguments by position

print('my name is {name} and i am {age} years old'.format(name = name,age = age))

#f-strings, this is available from python 3.6 and imo this one is the faster 

print(f'hello my name is {name} and i am {age} years old')

s='hello world'

#capitalize

print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(len(s))
print(s.replace('world','how are you'))
sub='w'
print(s.count(sub))
print(s.startswith('hello'))
print(s.endswith('you'))
print(s.split())
print(s.find('r'))
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())

