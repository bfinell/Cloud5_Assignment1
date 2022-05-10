#!/usr/bin/python
import time
import sys
from collections import Counter
start = time.perf_counter()
words=[]
current_word = None
current_count = 0
word = None
three_word_count = 0
five_word_count = 0
counter = Counter()
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError as v:
        print(v)
    if current_word == word:
        current_count += count
        counter[current_word] = current_count
    else:
        if current_word:
            if len(word) == 3: three_word_count +=1
            elif len(word) == 5: five_word_count +=1
            counter[current_word]=current_count
        current_count = count
        current_word = word
for words in counter.most_common(100):
    print('%s\t%s' % (words[0] ,words[1]))
print("three letter words: %s five letter words: %s" % (three_word_count,five_word_count)) 
stop = time.perf_counter()
print ('%.4f' % (stop-start),"seconds")
