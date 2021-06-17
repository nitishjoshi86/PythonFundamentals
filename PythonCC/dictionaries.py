#dictionary is a collection which is unordered,changeable and indexed, no duplicate members like sets

person = {
    'first':'john',
    'last':'carter',
    'age':30
}
person2 = dict(first = 'sara',last = 'willem')

print(person,type(person))
print(person2,type(person2))

print(person['first'])
print(person2['last'])

print(person2.get('last'))
person['phone'] = '987654321'
print(person)
print(person.keys)

print(person.items())
person3=person.copy()
person3['city'] = 'calgary'
print(person3)


del(person3['city'])
print(person3)
person3.pop('phone')
print(person3)
person3.clear()
print(person3)

print(len(person2))

people = [
    {'name':'mike','age':30},
    {'name':'kevin','age':23}
]
print(people[1]['name'])