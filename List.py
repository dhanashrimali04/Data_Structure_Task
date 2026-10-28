# #List CURD( Create, Update, read, Delete) Methods

animals = ['cat', 'dog', 'horse', 'monkey', 'lion', 'Deer']
print(animals)

# To add elements in list by : 1] append(), 2] insert(), 3] extend()
 
animals.append("Camel")
print(animals)

animals.extend(['panda', 'Cow'])
print(animals)

animals.insert(3,'Beer')
print(animals)

# to delete an elements  from list 

animals.pop(-2)
print(animals)

animals.remove('monkey')
print(animals)

# to update an elements from list
animals[1] = 'monkey'
print(animals)

# Reversing thi list

animals.reverse()
print(animals)

capitalized = [animals.capitalize() for animals in animals]
print(capitalized)