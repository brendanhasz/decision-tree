# bagdt.py
# Build Bootstrap aggregation model

import sys
from bagdt_utils import *

#Build decision tree list from passed file
if len(sys.argv)==3:
    num_trees = 11 #by default, use 11 trees
    build_bagged_dt(sys.argv[1], sys.argv[2], num_trees)
else:
    print "\nUSAGE: python bagdt.py <training_filename> <dcn_tree_filename>\n\n"

