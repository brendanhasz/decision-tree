# builddt.py
# Builds a decision tree from a file

import sys
from dt_io import *
from Tree import *
from info_funcs import *


def ID3(examples, attributes):
    '''
    Performs the Interactive Dichotomiser 3 algorithm on a list of examples
    and a list of lists of attributes
    '''
    root = Tree()

    #ID3 algorithm
 
    return root


def parse_training_file(filename):
    '''
    Parses an input file into a list of example classes and list of lists of
    attributes
    '''
    data = []
    thefile = open(filename, 'r')
    [[data.append([l.strip().split(',')[0], l.strip().split(',')[1:]])] for l in thefile]
    thefile.close()
    examples = []
    attributes = [[] for e in data[0][1]]
    for e in data:
        examples.append(e[0]) #example class
        for i in range(0,len(e[1])):
            attributes[i].append(e[1][i])            
    return examples, attributes


def build_decision_tree(train_data_fn, dt_fn):
    print "Building decision tree for "+train_data_fn+" ..."
    examples, attributes = parse_training_file(train_data_fn) #Parse input
    dt = ID3(examples, attributes) #Run decision-tree building ID3 algorithm
    save_dt(dt, dt_fn) #Save the decision tree
    print "Built decision tree for "+train_data_fn+" saved in "+dt_fn


#Build decision tree from passed file
build_decision_tree(sys.argv[1], sys.argv[2])


