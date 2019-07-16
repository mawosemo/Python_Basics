Sparta_clients =  ['ASOS',' BBC',' MEN IN BLACK ','Galactic  Empire','KGB', 'Rebel Alliance','The Kingsmen','S.H.I.E.L.D', 'Avengers']
#
# #y =
#  #print(y)
# #     #let us use interpolation
# A = f" {Sparta_clients[0]}, is a cool client of sparta "
# print(A)
# B = f" {Sparta_clients[1]}, is a cool client of sparta "
# print(B)
# C = f" {Sparta_clients[2]}, is a cool client of sparta "
# print(C)
# D = f" {Sparta_clients[3]}, is a cool client of sparta "
# print(D)
# E = f" {Sparta_clients[4]}, is a cool client of sparta "
# print(E)
G = Sparta_clients[5] + " is a cool client of alliance"
print(G)
first_name = input('what is your name?')
last_name = input('No your full name, ADD YOUR SURNAME FOOL?')
full_name = first_name+ ''+ last_name
hp = int(input("Mew said 'what's the percentage of his hp? "))
if hp >= 30:
    print('the force is strong with this one')
elif hp <= 30:
    print("WHATS UP FOOL, I'M DYING OUT HERE")

Pika={
    'hero': full_name,
  'beginning': ' In the beginning there was hero called ',
  'middle':'is 17.4 years old, he had the following pokemon pikachu,charmander,Squirtle,Mewtwo,and was always grumpy',
  'end':'he died at age 17.5',
}
#Access infomation using the keys
print(Pika['beginning']+ Pika['hero'])
print(Pika['hero']+Pika['middle'])
print(Pika['hero']+Pika['end'])