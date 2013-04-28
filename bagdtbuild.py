# bagdt.py
# Build Bootstrap aggregation model

import sys
from bagdt_utils import *

#Build decision tree list from passed file
if len(sys.argv)==3:
    print "Building bootstrap aggregate model from "+sys.argv[1]
    num_trees = 100 #by default, use 100 trees
    build_bagged_dt(sys.argv[1], sys.argv[2], num_trees)
    print "Done.  Bootstrap aggregate model saved as "+sys.argv[2]
else:
    print "\nUSAGE: python bagdtbuild.py <training_filename> <dcn_tree_filename>\n\n"

