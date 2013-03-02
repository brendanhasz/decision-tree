# build_dt.py
# Builds a decision tree from a file

import sys
from math import log
from dt_io import *
from Tree import *


#Build decision tree from passed file
build_decision_tree(sys.argv[1], sys.argv[2])


def build_decision_tree(train_data_fn, dt_fn):
    print "Building decision tree for "+train_data_fn+" ..."
    examples = parse_training_file(train_data_fn) #Parse input
    dt = ID3(exampes) #Run decision-tree building ID3 algorithm
    save_dt(dt, dt_fn) #Save the decision tree
    print "Built decision tree for "+train_data_fn+" saved in "+dt_fn


def ID3(examples):
    root = Tree()

    #ID3 algorithm
 
    return root


def info_gain(Y, A):
    
def entropy(Y):
    thesum = 0
    yl=len(Y)
    for e in set(Y):
        pyi = len([v for v in Y if v==e])/float(yl)
        thesum = thesum + pyi*log(1/pyi,2)
    return thesum


def parse_training_file(filename):
    data = []
    thefile = open(filename, 'r')
    [[data.append([l.strip().split(',')[0], l.strip().split(',')[1:]])] for l in thefile]
    file.close()
    return data
