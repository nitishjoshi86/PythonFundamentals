#variables are containers for values to be stored
""" variables are case sensitive and 
must start with a letter or an underscore 
they also can have numbers but cannot start with """


#X=2 #both variables x,X are different. variable type is int
#y=2.5 #this is type float
#name='John' #this is type string
#is_cool=True # boolean type variable

#muliple assignment
x,y,name,is_cool = (1,2.5,'John',True)

print('hello')
print(x,y,name,is_cool)

#basic math
a = x*y
b = x+y
c = x/y
d = x-y
print(a,b,c,d) 
#python is very simple because of its syntax if we consider basics, learning curve of python fundamentals is very short

#casting
x = str(x)
y = int(y)
z = float(y)
print(type(z),z)

