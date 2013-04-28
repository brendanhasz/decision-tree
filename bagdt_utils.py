# bagdt_utils.py
# Building and applying utilities for Bootstrap aggregation model

import sys
from dt_io import *
from Tree import *
from random import randrange
from builddt_utils import ID3
from builddt_utils import parse_training_file
from applydt_utils import *

perc_train = 0.8 #percent of training samples to use for making this tree

def apply_bagged_dt(test_fn, dt_fn, out_fn):
    att = parse_test_file(test_fn)
    baglist = load_dt(dt_fn)
    outcomes = [most_common([classify(a,baglist[i]) for i in range(0,len(baglist))]) for a in att]
    outcomes = [c if c!=None else most_common(outcomes) for c in outcomes] #cleanup
    write_output_file(outcomes, att, out_fn)


def build_bagged_dt(train_fn, dt_fn, num_trees):
    examples, attributes = parse_training_file(train_fn) #parse input
    baglist = []
    for k in range(0,int(num_trees)): #loop, each time
        print "Building tree number "+str(k+1)+" of "+str(int(num_trees))
        ex_s = []
        att_s = [[] for e in attributes]
        for j in range(1,int(len(examples)*perc_train)): #build sampled dataset
            r = randrange(0,len(attributes[0]))
            ex_s.append(examples[r])
            [att_s[i].append(attributes[i][r]) for i in range(0,len(attributes))]
        baglist.append(ID3(ex_s,att_s,range(0,len(attributes)),1)) #run ID3 + append
    save_dt(baglist,dt_fn) #save list of trees


