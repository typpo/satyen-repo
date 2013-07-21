# Reads CSV of name, score pairs and creates a data structure for quick lookup
# of names matching "<query>." or "<query>_"
# usage:
# serialize.py <csv_path> <output_path>

import sys
import pickle

f = open(sys.argv[1], 'r')

SPECIAL_CHARS = set(['.', '_'])

lookup_table = {}
num_entries = 0
num_total = 0
for line in f.readlines():
  num_total += 1
  name, idx = line.split(',')
  has_special_index = False
  for i in range(len(name)):
    c = name[i]
    if c in SPECIAL_CHARS:
      # Index the string up to this specific position, because it matches the
      # desired query format.
      lookup_table[name[:i]] = { 'score': int(idx), 'name': name }
      num_entries += 1

  if num_total % 50000 == 0:
    print '%d (%d) ...' % (num_total, num_entries)

#print lookup_table
print num_entries, 'entries total for', num_total, 'lines total'

print 'Writing serialized file...'
pickle.dump(lookup_table, open(sys.argv[2], 'w'))

print 'Done.'