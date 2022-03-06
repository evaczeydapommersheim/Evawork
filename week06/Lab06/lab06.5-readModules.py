# function to read in modules until the user enters blank

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

    return modules  #returning the list of modules