#!/usr/bin/env python
# A module that quickly looks up variable names and scores generated by
# serialize.py.
#
# This can be used as a module in a server by directly calling run_query, or
# you can play with it via terminal.
#
# usage:
# query.py <serialized_file>
#

import sys
import pickle

if len(sys.argv) < 1:
  print 'usage: query <serialized_path>'
  sys.exit(1)

print 'Loading lookup table...'
lookup_table = pickle.load(open(sys.argv[1], 'r'))
print 'Loaded.'

def run_query(query):
  print 'Searching for "%s"' % (query)
  return lookup_table.get(query, None)

if __name__ == "__main__":
  print 'Ready.'
  print 'This program matches queries matching variables of the form "<query>." and "<query>_"'
  print
  while True:
    query = raw_input('Search for a variable: ')
    for result in run_query(query):
      print '%s: %s' % (result['name'], result['score'])
