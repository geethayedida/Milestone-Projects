#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 4:
        userid, itemid, rating, timestamp = data
        print '%s\t%s\n' % (int(itemid), 1)
