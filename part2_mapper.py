#!/usr/bin/python
import sys
# cat .\apache_log_UTF8.txt |python part2_mapper.py |sort |python part2_reducer.py
for line in sys.stdin: 
    line = line.strip()
    print(line)