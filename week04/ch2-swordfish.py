# Automate the boring stuff with python Chapter 2 while loop exercise
# Author: Eva Czeyda-Pommersheim

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What  is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')