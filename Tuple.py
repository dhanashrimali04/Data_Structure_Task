family = ('Mumma', 'Pappa','Brother')
print("Original tuple:", family)

# #len()
print(len(family))

# #reverse
reverse = family[::-1]
print(reverse)

#access an element in tuple 
print(family[-1])
print(family[1])
 
# Add an element
temp = list(family)
temp.append("Sister")
family = tuple(temp)
print(family)

#Update an Element in Tuple 
temp2 = list(family)
temp2[1] = "Father"
family = tuple(temp2)
print(family)

#Delete an Element in Tuple 
temp3 = list(family)
temp3.remove("Brother")
family = tuple(temp3)
print(family)
