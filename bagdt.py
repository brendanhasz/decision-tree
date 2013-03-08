# bagdt.py
# Build Bootstrap aggregation model

import sys
from dt_io import *
from Tree import *
from random import randrange
from builddt import *

def build_bagged_dt(train_fn, dt_fn, num_trees):
    print "Building Bootstrap Aggregate model for "+train_fn+" ..."
    examples, attributes = parse_training_file(train_fn) #parse input
    baglist = []
    for i in range(1,int(num_trees)): #loop, each time
        ex_s = []
        att_s = [[] for e in attributes]
        for j in range(1,int(len(examples)*0.9)): #build sampled dataset
            r = randrange(0,len(attributes[0]))
            ex_s.append(examples[r])
            [att_s[i].append(attributes[i][r]) for i in range(0,len(attributes))]
        baglist.append(ID3(ex_s,att_s,range(0,len(attributes)),1)) #run ID3 + append
    save_dt(baglist,dt_fn) #save list of trees
    print "Built Bootstrap Aggregate model for "+train_fn+" saved in "+dt_fn


#Build decision tree list from passed file
if len(sys.argv)==3:
    num_trees = 11 #by default, use 11 trees
    build_bagged_dt(sys.argv[1], sys.argv[2], num_trees)
else:
    print "\nUSAGE: python bagdt.py <training_filename> <dcn_tree_filename>\n\n"

