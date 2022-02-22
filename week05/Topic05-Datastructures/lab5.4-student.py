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

print("Student:", list(student.items())[0][1]) 
# Source RealPython built-in dictionary methods, .items() creates a list of tuples of the key-value pairs, which then can be listed based on their index, 
# #(StudentName : Mary is the first element of this list (index 0)=[0] and the second [] determines if it shuold be the key [0] or its value [1] returned.
for module in student['modules']: 
    #as there are more than one modules, identify key as plural and use for loop to list the different courses and corresponding grades
    print("\t {} \t: {}".format(module['courseName'], module['grade']))

