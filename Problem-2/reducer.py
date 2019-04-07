#!/usr/bin/env python
"""reducer.py"""
from operator import itemgetter
import sys
import json
import ast


order = {"1":"1"}
line_item={"1":"1"}

def create(key, value):
    if(key == 'order'):
        order[str(value[1])] = value
    else:
        if value[1] not in line_item.keys():
            line_item[str(value[1])] = [value]
        else:
            line_item[str(value[1])].append(value)
            



def final_list(order, line_item):
    li = []
    for i in line_item.keys():
        for j in order.keys():
            if i == j:
                for _ in line_item[j]:
                    li = []
                    li.append(order[j])
                    li.append(_)
                    print li
                    print "---------------"

# input comes from STDIN

count = 0
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, value = line.split("\t", 1)
    new_val = value.split(", ")
    create(key, new_val)


final_list(order, line_item)

    