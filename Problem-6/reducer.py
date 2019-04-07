#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

a = []
b = []
temp1 = [0,0,0,0,0]
temp2 = [0,0,0,0,0]
temp3 = [0,0,0,0,0]
temp4 = [0,0,0,0,0]
temp5 = [0,0,0,0,0]

temp6 = [0,0,0,0,0]
temp7 = [0,0,0,0,0]
temp8 = [0,0,0,0,0]
temp9 = [0,0,0,0,0]
temp10 = [0,0,0,0,0]



# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    words = line.split(", ")

    words[0] = words[0].strip("[")
    words[0] = words[0].strip("\"")

    words[3] = words[3].strip("]")
    words[1] = int(words[1])
    words[2] = int(words[2])
    words[3] = int(words[3])
    
    
    if words[0] == "a":
        if words[1] == 0:
            temp1.insert(words[2],words[3])
        if words[1] == 1:
            temp2.insert(words[2],words[3])
        if words[1] == 2:
            temp3.insert(words[2],words[3])
        if words[1] == 3:
            temp4.insert(words[2],words[3])
        if words[1] == 4:
            temp5.insert(words[2],words[3])
    else:
        if words[1] == 0:
            temp6.insert(words[2],words[3])
        if words[1] == 1:
            temp7.insert(words[2],words[3])
        if words[1] == 2:
            temp8.insert(words[2],words[3])
        if words[1] == 3:
            temp9.insert(words[2],words[3])
        if words[1] == 4:
            temp10.insert(words[2],words[3])
        

a.append(temp1)
a.append(temp2)
a.append(temp3)
a.append(temp4)
a.append(temp5)

b.append(temp6)
b.append(temp7)
b.append(temp8)
b.append(temp9)
b.append(temp10)


result = [[sum(x*y for x,y in zip(a_row,b_col)) for b_col in zip(*b)] for a_row in a]

for i in result:
    for j in i:
        if j != 0:
            print [result.index(i), i.index(j), j]


