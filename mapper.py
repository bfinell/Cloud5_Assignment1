#!/usr/bin/python
import sys
# cat input.txt | python3 mapper.py | sort -k1,1 | python3 reducer.py | python3 sorter.py > output.txt
for line in sys.stdin: 
    line = line.strip()
    words = line.split() 
    for word in words: 
        print('%s\t%s' % (word, 1))
