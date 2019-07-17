
import sys
import os
import json

def getfilename(inputdata):
    with open(inputdata,"r") as inputread:
        inputdict=json.loads(inputread.read())
    for i in inputdict:
        myvalueprint(i)

def myvalueprint(inputdata2):
        for k,v in inputdata2.items():
            if k == 'file':
                print("File name is {}".format(v))
            elif isinstance(v,dict):
                myvalueprint(v)
            else:
                print("There is no file name in the dictionary")

if __name__ == '__main__':
    inputdata= sys.argv[1]
    getfilename(inputdata)
    #myvalueprint(inputdata)
