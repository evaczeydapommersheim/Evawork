#Combine all function created until now under Lab06.3

#Author: Eva Cz-P
import json

filename = "storedata.json"
students = []
def displayMenu():
    print('What would you like to do?')
    print('\t (a) Add new student')
    print('\t (v) View students')
    print('\t (s) Save students')
    print('\t (l) Load students')
    print('\t (q) Quit')
    choice = input('Type one letter (a/v/s/l/q): ').strip()

    return choice

def doAdd(students):
    student = {}
    student['name'] = input('Enter name: ')
    student['modules'] = readModules()
    students.append(student)
    return students

def readModules():
    modules = []
    moduleName = input("\tEnter the first module name (blank to quit):").strip() 
    
    #The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)

    while moduleName != "":
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
    for student in students:
        print(student["name"])
        displayModules(student["modules"])
    return students

def doSave(students):
    with open(filename, "a+t") as f:
        json.dump(students,f)
    print("Data saved")
    return students

def doLoad(students):
    with open(filename, "rt") as f:
        return json.load(f)

menuChoice = {
    'a' : doAdd,
    'v' : doView,
    's' : doSave,
    'l' : doLoad
}
#Main Program

choice = displayMenu()
while choice != "q":
    if choice in menuChoice:
        students = menuChoice[choice](students)
    else:
        print ("invalid choice try again")

    choice = displayMenu()

print ("goodbye")
