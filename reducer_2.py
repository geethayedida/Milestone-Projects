#!/usr/bin/env python
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
print_count = 0
movie_review_count = []

for line in sys.stdin:
        if line.strip():
                word,count = line.strip().split()
                count = int(count)
                if current_word == word:
                        current_count += count
                else:
                        if current_word:
                                movie_review_count.append((int(current_word), current_count))
                                current_count = count
                        current_word = word
if current_word == word:
    movie_review_count.append((int(current_word), current_count))
movie_review_count =  sorted(movie_review_count,key = lambda x:(-x[1],x[0]))
f = open("/home/ubuntu/inputfiles/ml-100k/u.item","r")
for i in range(5):
        current_movie =  movie_review_count[i]
        movie = current_movie[0]
        rating = current_movie[1]
        print "The movie " + str(movie) + " has " + str(rating) + " ratings"
f.close()
