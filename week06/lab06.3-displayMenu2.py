#Write a function that prints out a menu of commands we can perform, 
# ie add, view and quit. The function should return what the user chose.


# Author: Eva CZ-P

def displayMenu():
    print('What would you like to do?')
    print('\t (a) Add new student')
    print('\t (v) View students')
    print('\t (q) Quit')
    choice = input('Type one letter (a/v/q): ').strip()

    return choice

def doAdd():        # doAdd function is defined
    print('In adding')

def doView():       # doView function is defined
    print('In viewing')

choice = displayMenu()
while (choice != 'q'):
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice != 'q':
        print('\n\nPlease enter a,v or q')
    choice = displayMenu()