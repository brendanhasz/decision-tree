# bagdt.py
# Build Bootstrap aggregation model

import sys
from dt_utils import build_bagged_dt

DEF_NUM_TREES = 100 #by default, use 100 trees
DEF_MAX_RECURSION = 10 #by default, use 10 levels of recursion in trees

#Build decision tree list from passed file
if len(sys.argv)==3:
    print "Building bootstrap aggregate model from "+sys.argv[1]
    build_bagged_dt(sys.argv[1], sys.argv[2], DEF_NUM_TREES, DEF_MAX_RECURSION)
    print "Done.  Bootstrap aggregate model saved as "+sys.argv[2]
elif len(sys.argv)==4:
    print "Building bootstrap aggregate model from "+sys.argv[1]+" with "+sys.argv[3]+" trees"
    build_bagged_dt(sys.argv[1], sys.argv[2], int(sys.argv[3]), DEF_MAX_RECURSION)
    print "Done.  Bootstrap aggregate model saved as "+sys.argv[2]
elif len(sys.argv)==5:
    print "Building bootstrap aggregate model from "+sys.argv[1]+" with "+sys.argv[3]+" trees and "+sys.argv[4]+" levels of recursion"
    build_bagged_dt(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    print "Done.  Bootstrap aggregate model saved as "+sys.argv[2]
else:
    print "\nUSAGE: python bagdtbuild.py <training_filename> <dcn_tree_filename> (<num_trees>) (<max_num_recursion>)\n\n"

