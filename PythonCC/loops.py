#for loop is used for iterating over a sequence (that is either a list,a tuple,a dictionary,a set, or a string)
#while loop execute a set of statements as long as a condition is true.


people = ['john','hog','shira','edward']

""" for person in people:
    print(f'current person:{person}')


for person in people:
    if person == 'shira':
        break
    
    print(f'current person:{person}')
for person in people:
    if person == 'shira':
        continue
    
    print(f'current person:{person}') """

""" for i in range(len(people)):
    print(people[i])
for i in range(0,11):
    print(f'Number:{i}') """

count = 0
while count<10:
    print(f'Count:{count}')
    count += 1
    