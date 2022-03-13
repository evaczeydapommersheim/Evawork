# messing with os module
# Author: Eva Cz-P

import os   #built in module in Python, more info in real python, messing around with operating system, checking if file exists.
# you can delete a file, check if it exists

filename = "test.txt"
if os.path.exists(filename):
    print(filename, "already exists")
    os.remove(filename)
else:
    print(filename, "does not exist do you want to create it?")
