#Data types

 #Computers are stupid
    #They don't understand data types and we need to be specific


# Strings
#Lists of characters bundled together in a specific order
# Using index
print('hello')
print('hello')
print(type('hello'))
        # #concatination
        # #Joins two strings together
string_a = 'hello there'
name_person = ' Luke cage'

print(name_person +' '+ string_a)



#useful methods
#finding length of a variable
print(len(string_a))
print(len(name_person))

#strip
#removes white spaces
string_num = ' 051660 '
print(type(string_num))
print(string_num)
print(string_num.strip())

#.split - it is a method for strings
# #it splits in a specific location and output a list(datatype
string_text = 'hello i need to go to the loo'
 split_string = string_text.split('o')
 print(split_string)
#
 print('please give us a strings ')
 user_input = input('Now!!! >>>>> ')
 print(user_input)
# # Get userinput and print first name and last name
#get user input
 first_name = input('what is your name?')
 #saveuser input to variable
 #get user last name and save it to variable
last_name = input('what is your name?')
# #Join the two
#     #let us use concactination
 full_name = first_name+ ' '+last_name
 print(full_name)
#     #let us use interpolation
 welcome_message = f"Hi {full_name}, you are very welcome!!!"
 print(welcome_message)

#print

# Count / lower/ upper / capitilize
text_example = "here is some text, with lot's of text"
#count
print(text_example.count('e'))
print(text_example.count('text'))

# Lower
print(text_example.lower())

#Upper
print(text_example.upper())

#Capitilize - only capitilize the first character of the string

print(text_example.capitalize())