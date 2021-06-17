#collection which is ordered and mutable, allows duplicate

numbers = [1,2,3,4,5,5,6]

fruits = ['apple','oranges','grapes','banana']

print(fruits[1])

print(len(fruits))

fruits.append('peaches')

fruits.remove('grapes')

fruits.insert(2,'watermelon')

fruits.pop(2)
fruits.reverse()

fruits.sort()

fruits.sort(reverse=True)

fruits[0] = 'blueberries'

print(fruits)