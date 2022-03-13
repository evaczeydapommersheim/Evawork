# this program creates a file count.txt with a content of "0".
# Author: Eva Cz-P.

with open("count.txt", "wt") as f:
    data = f.write("0")
    print("File count.txt is created")