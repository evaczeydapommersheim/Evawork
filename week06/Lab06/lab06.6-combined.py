#Combine all function created until now under Lab06.3

#Author: Eva Cz-P

def displayMenu():
    print('What would you like to do?')
    print('\t (a) Add new student')
    print('\t (v) View students')
    print('\t (q) Quit')
    choice = input('Type one letter (a/v/q): ').strip()

    return choice

def doAdd(students):
    currentStudent = {}
    currentStudent['name'] = input('Enter name: ')
    currentStudent['modules'] = readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the first module name (blank to quit):").strip() 
    
    #The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)

    while moduleName != " ":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\tEnter grade:"))
        modules.append(module)      #add entered module to the list [] of modules
        moduleName = input("\tEnter the next module name (blank to quit):").strip()     #adding another module name

    return modules

def displayModules(modules):
    print("\tName   \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"]))

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

#Main Program
students = []
choice = displayMenu()
while (choice != 'q'):
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice != 'q':
        print('\n\nPlease enter a,v or q')
    choice = displayMenu()