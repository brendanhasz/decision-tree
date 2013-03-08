# bagdt.py
# Build Bootstrap aggregation model

import sys
drom dt_io import *
from Tree import *

def build_bagged_dt(train_fn, dt_fn):
    print "Building Bootstrap Aggregate model for "+train_fn+" ..."
    examples, attributes = parse_training_file(train_fn) #parse input
    baglist = []
    #loop, each time
        #build sampled dataset
        #run ID3
        #append tree to list of trees
    #save list of trees
    print "Built Bootstrap Aggregate model for "+train_fn+" saved in "+dt_fn

#Build decision tree list from passed file
if len(sys.argv)==3:
    build_bagged_dt(sys.argv[1], sys.argv[2])
else:
    print "\nUSAGE: python bagdt.py <training_filename> <dcn_tree_filename>\n\n"

