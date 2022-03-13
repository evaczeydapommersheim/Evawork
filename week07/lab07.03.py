#  Writes a function that will store a simple Dict to a file as JSON. 
# Author: Eva Cz-P.

import json
filename = "testdict.json"
sample = dict(name="fred", age=31, grades=[1,34,55])
def writeDict(obj):
    with open(filename,'wt') as f:
        json.dump(obj,f)
writeDict(sample)
