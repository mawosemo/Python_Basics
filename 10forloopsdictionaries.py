# # For loop - Using dictionaries / Hashes
#
# syntax
# #   for <placeholder> in list<dict>:
# #      run block of code

dict_data = {
    'name': 'Bronson',
    'money':200
}
# #we use key to access the values of our dictionary
# print(dict_data['key'])

for key in dict_data:
    #when we iterate over a hash /fictionary
    #the p;lace holder, holds an indiviual key during each iteration
    print(key + ':', dict_data[key])


embeded_dict_data = {
    1: {
    'name': 'Bronson',
    'money':200
    },
    2: {
    'name': 'tania',
    'money': 300
    },
    3: {
    'name': 'tylor',
    'money': 400
    },
}
for key in embeded_dict_data:
    print(key)
    #Or
for key2 in embeded_dict_data.values():
    print(key2)
    print(type(key2))
    embeded_dict_data={

        1:{...},
        2:{...},
        3:{...}
    }

for key in embedded_dict_data:
    











