#!/usr/bin/env python
import sys

txt = open(sys.argv[1]).read().decode('ebcdic-cp-be')

for i in xrange(0, len(txt), 80):
  print txt[i: i + 80]
