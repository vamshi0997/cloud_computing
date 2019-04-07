#!/usr/bin/env python
"""mapper.py"""

import json
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = json.loads(line.decode("utf-8"))
    check = line[0].strip()
    key = line[1].strip()
    print '%s%s' %(check+"\t", line)
        