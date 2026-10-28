family = { "Mother": "Aai", 
           "Father": "Baba",
           "Brother": "Bhau",
           "Sister": "Tai"}

print(family)

#Acces Elements
print(family["Mother"])
print(family["Brother"])
print(family["Sister"])
print(family["Father"])


#Update Dict
family["Father"] = "Pappa"
print(family)

# Add Element
family["Cousin"] = "Dada"
print(family)

# Delete Elements
del family['Cousin']
print(family)

#Get all Keys
print(family.keys())

#Get all values 
print(family.values())

#Get all items 
print(family.items())





