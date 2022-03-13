# Week07 quizz answers
# Author: Eva Cz-P.

#a.) as the file is assumed to not exist it cannot be read, it shouold return an error
#b.) 7, 14
#c.) "another line"
#d.) test d another line

with open("test-b.txt", "w") as f:
    data = f.write("test b\n") #return the number of characters written
    print(data)

with open("test-b.txt", "w") as f2:
    data = f2.write("another line \n")
    print(data)

with open("test-d.txt", "wt") as f3:
    data = f3.write("test d\n")
    print(data)

with open("test-d.txt", "at") as f4:
    data = f4.write("another line \n")
    print(data)

