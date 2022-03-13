# messing with files
# Author: Eva CZ-P
filename = "test.txt"
with open(filename, 'w+t') as f:
    f.write('Hello World!')
    f.seek(0)
    data = f.readline()
    print(data)
print("Done")

#filename = "testread.txt"
#with open(filename, "rt") as f:
#   data = f.read()
#   print(data)

with open("messingwithfiles.py", "rt") as f:
    for line in f:
        # print(line[:-1])
        print(line, end='')