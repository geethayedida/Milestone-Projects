#!/usr/bin/env python
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    if len(line) == 2:

        word,count = line.strip().split()

        count = int(count)

        if current_word == word:
            current_count += count
        else:
            if current_word:
                print '%s\t%s' % (current_word, current_count)
            current_count = count
            current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s' % (current_word, current_count)
