#!/usr/bin/env python
# Reads CSV of name, score pairs and creates a data structure for quick lookup
# of names matching "<query>." or "_<query>."
#
# usage:
# serialize.py <csv_path> <output_path>
#

import sys
import cPickle as pickle

if len(sys.argv) < 2:
  print 'usage: serialize <csv_path> <serialized_output_path>'
  sys.exit(1)

f = open(sys.argv[1], 'r')


lookup_table = {}
num_entries = 0
num_total = 0

def put_in_index(lookup_table, index_on, name, score):
  lookup_table.setdefault(index_on, [])
  # Some queries can match multiple, so we keep a list in no particular
  # order..
  lookup_table[index_on].append({ 'score': score, 'name': name })

for line in f.readlines():
  num_total += 1
  name, score = line.split(',')
  has_special_index = False
  prev_underscore_idx = -1
  for i in range(len(name)):
    c = name[i]
    if c == '.':
      # index <query>.
      index_on = name[:i]
      put_in_index(lookup_table, name[:i], name, int(score))
      num_entries += 1

      # index _<query>. if there was a previous underscore
      if prev_underscore_idx > -1:
        index_on = name[prev_underscore_idx+1:i]
        if index_on != '':
          put_in_index(lookup_table, index_on, name, int(score))
        num_entries += 1

    if c == '_':
      prev_underscore_idx = i

  if num_total % 50000 == 0:
    print '%d (%d) ...' % (num_total, num_entries)

print num_entries, 'entries total for', num_total, 'lines total'

# This part can be a bit slow; takes about 46s on my computer.
# But we only need to do this once, so I preferred to optimize lookup
# rather than creation..
print 'Writing serialized file...'
pickle.dump(lookup_table, open(sys.argv[2], 'w'), pickle.HIGHEST_PROTOCOL)

print 'Done.'
