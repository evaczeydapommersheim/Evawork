# This is to create a file for week07 weekly task moby-dick.txt

# Author: Eva Cz-P.

filename = "moby-dick.txt"
with open (filename, "w+t") as f:
    f.write(str("Some years ago never mind how long precisely having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen, and regulating the circulation."))
    f.seek(0)
    data = f.readline()
    print(data)
print("Done")


