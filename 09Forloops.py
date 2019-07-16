import time
# # For loops in python
# # used to iterate over collections . list and directories
# #
# #
# # syntax
#   for <placeholder> in list:
#       do something
# #w#####place holder in a variable that it's scopeis limited to the loop or function
#
# x_crazy_landlord = ['cruella de vill','Donald Duck','popeye the maltese']
# counter =  0
# print('Starting loop')
# for landlord in x_crazy_landlord:
#     print('hello')
#     print(landlord)
#     print(counter)
#     counter += 1
# # print('loop ended')
#
# x_crazy_landlord = ['cruella de vill','Donald Duck','popeye the maltese']
#
# counter = 1
# for landlord in x_crazy_landlord:
#     print(counter,'-', landlord)
#     counter += 1
#
## Further loops

#list_data = [1, 2, 3, 4, 5]

# for num in list_data:
#     print(num)
# embedded_list = [[1, 2, 3 ],[5, 6, 7]]
#
# for data in embedded_list:
#     print(data)
#     time.sleep(2)
#     for number in data:
#         print(number)
# #     time.sleep(2)
# Sparta_clients =  ['ASOS','BBC','MEN IN BLACK ','Galactic  Empire','KGB', 'Rebel Alliance','The Kingsmen','S.H.I.E.L.D', 'Avengers','Spartans Assemble' ]
# embedded_spartan = [['joj']]
#
# for x in Sparta_clients:
#     print('client id -',x)

list_scores = [1, 10, 3, 4, 5, 6]

for num in list_scores:
    result_percent = num / 10 * 100
    print(result_percent)
list_embed_scores = [[1, 10, 3], [4, 5, 6]]

for ind_list in list_embed_scores:
    print(ind_list)
    for num in ind_list:
        print(num*2)
