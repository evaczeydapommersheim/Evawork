# This program stores a students name and a list of her courses and grades in a dict and prints out her data

# Author: Eva Czeyda-Pommersheim



student = {
    'studentName' : 'Mary',
    'modules' : [{
        'courseName' : 'Programming',
        'grade' : 45
    },{
        'courseName' : 'History',
        'grade' : 99
    }
    ]
}

print("student: {}".format(student["studentName"]))
module = input("Enter your module name: ")
print(module)

for module in student["modules"]:
    while True:
        module != " "
        print("\t {}".format(module["courseName"]))
        break