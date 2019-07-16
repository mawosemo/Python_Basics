# While loops
#
# syntax
# while<condition>
#     Block of code
#         **optional** if <condition >
#                             break
#
# counter = 0
#
# while counter < 28:
#     print("BOOM MY AGE IS:",counter)
#     counter += 1
#
# print('end')
#
# while True:
#     print('Welcome to the loop')
#     word = input('Tell me a word').strip().lower()
#     # break#
#     if word == 'bananas':
#         print('you cracked the code')
#         break
#     else:
#         print('HAHAHAHAHAHAHAHA YOU SUCK ')
#         print('HAHAHAHAHAHAHAHA YOU SUCK ')
#
# alert(
#     "You are Ollie, a likeable young guy in search of love. Our story begins when Ollie comes across an attractive young woman on Tinder...");
#
# var
# swipe_choice = prompt("Will you swipe left or right?: (1)Right (2)Left");
match = int(input('Welcome to Tinder, please choose a response ->'))
if match == 1:
    print("She swiped right, too! It's a match! Now don't screw this up...")
    elif match == 2:2
    print("Hmm, perhaps Ollie's standards are a little high... GAME OVER")
    else:
    print('invalid response')
# throw
# "StandardsTooHighError";
#
#
#
#
#
#
#
#
#
#
#
# // CHAPTER
# TWO //
# alert("She messages you and asks for a date! But she wants you to pick the type of restaurant.")
#
# var
# food_choice = prompt("What kind of food will you choose?: (1)Italian (2)Curry (3)Pub grub");
#
# // Write
# an if / else if / else statement to check which food you choose - if it's Italian, execute the first alert, if it's Curry, execute the second with the throw, or if it's Pub grub, execute the third
#
# alert("Ah, molto bella!");
#
# alert("Curry on a first date!? What were you thinking? GAME OVER");
# throw
# "RiskyFoodError";
#
# alert("Lovely jubbly.");
#
# // CHAPTER
# THREE //
# var
# drunk_guess = prompt(
#     "You meet at the restaurant and after an hour, everything seems to be going fine! However, you notice your date might have had a bit much to drink... what do you think? (Enter true or false)");
#
# alert(
#     "Whatever you say! Oh no, now she's asking how old you think she is! Maybe she's had too much drink to really notice what you say...")
# var
# age_guess = prompt("What age will you say?");
#
# // Write
# an if / else statement
# including
# the or operator - if your
# age_guess is under
# 30
# OR
# your
# drunk_guess is true, execute
# the
# first
# alert, but if NEITHER
# of
# those
# conditions
# are
# met, execute
# the
# second
# with the throw
#
# alert("She smiles and shrugs. 'I'll never tell!' Phew, that was a close one!");
#
# alert("Uh, I think you might have miscalculated somewhere... GAME OVER")
# throw
# "OffensiveError";
#
# // CHAPTER
# FOUR //
# alert("The rest of the evening goes wonderfully and soon, the bill arrives. Yikes! £100!?")
# var
# pay_choice = prompt("What will you do?: (1)Say you left your wallet at home. (2)Offer to pay.");
# var
# money_in_wallet = parseInt(prompt("Wait... how much money do you actually have?"));
#
# // Write
# an if / else statement
# including
# the and operator - if your
# pay_choice is to
# Offer
# to
# pay
# AND
# the
# money_in_wallet is over or equal
# to
# 100, execute
# the
# first
# alert, but if EITHER
# of
# those
# conditions
# isn
# 't met, execute the second with the throw
#
# alert("How very gallant of you! She seems impressed...")
#
# alert("Sorry, nobody likes a cheapskate.")
# throw
# "Don'tBeSoTightError";