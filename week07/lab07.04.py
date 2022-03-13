# funtion that will read in the content of a dict object.
# Author: Eva Cz-P.

import json
filename = "testdict.json"

def readDict():
    with open(filename, "rt") as f:     #i could also leave out the "rt" as this is the default
        return json.load(f)

dict = readDict()
print(dict)
