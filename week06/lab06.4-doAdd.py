#Write a function that prints out a menu of commands we can perform, 
# ie add, view and quit. The function should return what the user chose.

# Author: Eva CZ-P
students = []
def readModules():
    return[]
def doAdd(students):
    currentStudent = {}
    currentStudent['name'] = input('Enter name: ')
    currentStudent['modules'] = readModules()

    students.append(currentStudent)
doAdd(students)     #testing that doAdd works

doAdd(students)
print(students)