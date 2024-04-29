import os

def readFromFile(filename):
    if not os.path.exists(filename):
        raise Exception("Bad File")
    infile = open(filename)
    line = infile.readline()
    return line

