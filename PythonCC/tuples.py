#tuples is a collection which is ordered and unmutable, duplicate members allowed
#set is a collection which is unordered and unindexed, no duplicate members

fruit = ('apples','grapes','oranges','watermelon')
fruits2 = tuple(('apples','oranges','cherries','peaches'))
#single values need trailing coma
print(fruits2,type(fruits2))
print(fruit[1])



print(len(fruits2))

fruit1 = {'apples','oranges','mango'}
print('apples' in fruit1)
fruit1.add('grape')
print(fruit1)
fruit1.remove('grape')
print(fruit1)

fruit1.add('apples')


print(fruit1)
