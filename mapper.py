#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 4:
        a, b, rating, c = data
        for i in data:
            print '%s\t%s\n' % (int(rating), 1)
    else:
        print "none"
