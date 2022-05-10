#!/usr/bin/python
from multiprocessing.sharedctypes import Value
from re import S
import sys
from collections import Counter
from tracemalloc import stop
words=[]
most_popular = []
current_word = None
current_count = 0
word = None
tot_size = 0
amount_of_requests = 0
counter = Counter()
for line in sys.stdin:
    line = line.strip()
    amount_of_requests+=1
    domain, size = line.split()[0],line.split()[-1]
    try:
        tot_size += (int(size)/(1024*1024*1024))
    except TypeError as t:
        continue
    except ValueError as v:
        continue

    if current_word == domain:
        current_count += 1
        counter[current_word] = current_count
    else:
        if current_word:
            counter[current_word]=current_count
        current_count = 1
        current_word = domain
for words in counter.most_common(15):
    print('%s\t%s' % (words[0] ,words[1]))
    try:
        int(str(words[0])[0])
    except TypeError as t:
        most_popular.append(str(words[0])+" :  "+str(words[1]))
    except ValueError as v:
        most_popular.append(str(words[0])+" :  "+str(words[1]))
    if (len(most_popular)>=5):
        break
print("total size in GB: %s" % (tot_size))
print("cost is: %.4f €" % (tot_size*0.08+0.001*amount_of_requests))
with open("part2_output","w") as f:
    for domains in most_popular:
        f.write(domains+"\n")