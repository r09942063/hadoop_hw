#!/usr/bin/env python
import sys

cur_word=None
cur_count=0
word=None

for line in sys.stdin:
    line=line.strip()
    word,count=line.split()

    if cur_word==word:
        cur_count+=1
    else:
        if cur_word!=None:
            print "%s\t%d"%(cur_word,cur_count)

        cur_word=word
        cur_count=1

print "%s\t%d"%(cur_word,cur_count)
