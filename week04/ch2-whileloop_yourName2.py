# Automate the boring stuff with python Chapter 2 while loop exercise (pg47)
# Author: Eva Czeyda-Pommersheim

name = ''
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you!')