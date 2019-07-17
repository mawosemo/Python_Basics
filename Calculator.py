# # Calculator
# def say_hello():
#     print('hello there')
#
# say_hello()
#
# def full_name(f_name, l_name):# these arguments can only be used in the block of code
#
#        full_name_var = f_name+' '+l_name
#        return full_name_var

def add(value1, value2):


  return (value1 + value2)

def subtract(value1, value2):
    return (value1 - value2)


def multiply(value1, value2):
    return (value1 * value2)

def divide(value1, value2):
    return int(value1 / value2)

def area(value1):
    value3 = value1*value1*3.14
    return float(value3*2.54)

value1 = int(input('please insert a number: '))
function = input('insert function ')
value2 = int(input('please insert another number: '))

if function == 'area':
    print('the area of a circle is ', area(value1))
elif function == '-':
    print('the following subtract is ', subtract(value1, value2))
elif function == '*':
    print('the following multiplication is ', multiply(value1, value2))
elif function == '/':
    print('the following division is ', divide(value1, value2))
elif function == '+':
    print('the following addition is ', add(value1, value2))
else:
    print('invalid response')