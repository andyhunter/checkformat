import sys
import os
import re

if len(sys.argv) < 2:
    print('no path')
    sys.exit()

pattern1 = re.compile(r'[^\s(]\)')
pattern2 = re.compile(r'\([^\s)]')
pattern3 = re.compile(r',[^ ]')
rules = {
    "no space before )": pattern1,
    "no space after (": pattern2,
    "no space after ,": pattern3
}

path = sys.argv[1]
file = open(path, 'r')
line = file.readline()
lineCount = 1
while line:
    for i in rules:
        match = rules[i].search(line)
        if match:
            print("line " + lineCount.__str__() + " : " + i)
    line = file.readline()
    lineCount += 1
