# List and Dictionaries
# List


# sometimes we just need to list our craxy x-pokemon:)
#because we don't want to work there
# this is how you make alist
# [] seperare items using,
# ['bananas', 'pine','gasoline']
# declaring a list and saving to variable
crazy_pokemon =  ['snorlax',' Jigglipuff',' Mewtwo']
print(crazy_pokemon)
print(type(crazy_pokemon))

print(len(crazy_pokemon))
print(crazy_pokemon[2])
print(crazy_pokemon[0])
#
# if you want to print the last in a list
# you have two option.
# array[lens(array) -1]
print(crazy_pokemon[len(crazy_pokemon)-1])

print(crazy_pokemon[2])

# re-assigning the value in a list, using the in dex
# we need to evlove  mewtwo to mewtree


print(crazy_pokemon)
crazy_pokemon[2] = 'Mewtree'
print(crazy_pokemon)

# appending a new crazy_pokemon
# we caught pigeotto

crazy_pokemon.append('pigeotto')
#inserting

crazy_pokemon.insert(0,'Rattata')
print(crazy_pokemon)

crazy_pokemon.insert(2,'Rattata')#shifts and adds
print(crazy_pokemon)

#Removing a record
crazy_pokemon.pop()
print(crazy_pokemon)

crazy_pokemon.pop(0)
print(crazy_pokemon)
# removingusing a filter

crazy_pokemon.remove('Rattata')
print(crazy_pokemon)

# list can have any data types

mixed_list = ['Jones',10,42,'John']
print(mixed_list)
print(type(mixed_list[0]), type(mixed_list[1]))

# Inception List
# list within A LIST
leo_d = ['first',2,['leo','d']]


print(leo_d[0])
print('accessing the index 2')
print(leo_d[2])
print(leo_d[2][1])
sub_array = leo_d[2]
print(sub_array)
print(sub_array[1])

#All of this is the same as
print(leo_d[2][0][1])























