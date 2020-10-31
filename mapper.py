#!/usr/bin/env python
import sys
import re
for line in sys.stdin:
    line=line.strip()
    words=line.split()
    time=re.compile("\d{2}/\w{3}/\d{4}")
    word_list=time.findall(str(words))
    for word in words:
        print '%s\t%s' % (word_list[0], 1)
