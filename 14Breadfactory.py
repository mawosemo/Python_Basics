# Our Bread Factory

def make_dough(ingredient1, ingredient2):
    if'wheat' in ingredient1 and 'water' in ingredient2:
        return 'dough'
    else:
        return 'wrong ingredients'


def bake_bread(semi_product):
    if semi_product=='dough':
        return 'bread'
    else:
        return 'wrong ingredients'


#Tests
print('called function make_doughwith wrong ingredient')
print('call function make_dough, expect dough to be returned')
print(make_dough('wheat','water')=='dough')

print('called function bake_bread with wrong ingredient')
print('call function bake_bread, expect bread to be returned')
print(bake_bread('dough') == 'bread')

print(make_dough('wheat', 'water'))
print(make_dough('cement', 'water'))