#class is blueprint for creating objects. object has properties and methods(functions), almost everything in python is an object

#create class

class user:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age


    def greeting(self):
        return f'my name is {self.name} and i am {self.age} years old'


    def hasbirthday(self):
        self.age += 1

#extend class
class customer(user):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def setbalance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'my name is {self.name} and i am {self.age} years old and the balance is {self.balance}' 
#init user object
nitish = user('nitish joshi','nitish@gmail',34)
#init customer object
ramesh = customer('ramesh pandya','ramesh@gmail.com',25)

ramesh.setbalance(590)


print(nitish.name)
print(nitish.email)
print(nitish.age)

nitish.hasbirthday()
print(ramesh.greeting())
print(nitish.greeting())