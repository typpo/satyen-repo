#!/usr/bin/env python
# Generates test data for Java Name Lookup problem
# usage:
# generate.py <path> <# sample lines>

import sys
import string
from random import choice, randint

if len(sys.argv) < 2:
  print 'usage: generate <path> <# sample lines>'
  sys.exit(1)

# http://docs.oracle.com/javase/specs/jls/se7/html/jls-3.html#jls-3.8
# Put in some more underscores and periods to test main use case...
# But I don't think valid java variable names contain periods.
ALLOWED_CHARS = string.letters + string.digits + '$' \
    + ('_' * 10) + ('.' * 10)

def random_varname(n=20):
  return ''.join([choice(ALLOWED_CHARS) for x in range(n)])

def generate_file(path, n):
  f = open(path, 'w')
  for i in range(int(n)):
    f.write('%s,%d\n' % (random_varname(), randint(0, 1e6)))
  f.close()
  print 'Done.'

if __name__ == "__main__":
  generate_file(sys.argv[1], sys.argv[2])
