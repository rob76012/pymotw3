#!/usr/bin/env python3
"""Load pickles from a file
"""
#end_pymotw_header

import pickle
import pprint
import sys

from pickle_dump_to_file_1 import SimpleObject

filename = sys.argv[1]

with open(filename, 'rb') as in_s:
    while True:
        try:
            o = pickle.load(in_s)
        except EOFError:
            break
        else:
            print('READ: %s (%s)' % (o.name, o.name_backwards))