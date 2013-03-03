# builddt.py
# Builds a decision tree from a file

import sys
from dt_io import *
from Tree import *
from info_funcs import *


def ID3(examples, attributes, attr_labels):
    '''
    Performs the Interactive Dichotomiser 3 algorithm on a list of examples
    and a list of lists of attributes
    '''
    root = Tree()
    if len(set(examples))==1: #if only 1 class of ie left, use it
        root.data = examples[0]
    elif len(attributes)<1: #if no attributes left, use most common
        root.data = most_common(examples)
    else:
        #Find attribute that best classifies examples
        maxinfo = 0
        for i in range(0,len(attributes)):
            thisinfo = info_gain(examples, attributes[i])
            if thisinfo>maxinfo:
                i_A = i
                maxinfo=thisinfo
        root.data = attr_labels[i_A] #Store node attribute label
        A = attributes[i_A]
        #For each possible value of max info attribute, add branch
        for v in set(A):
            child = Tree()
            child.data = v
            root.addchild(child)
            E_v = [examples[i] for i in range(0,len(A)) if A[i]==v]
            if len(E_v)<1:
                leaf = Tree()
                leaf.data = most_common(examples)
                child.addchild(leaf)
            else:
                 child.addchild(ID3(E_v, all_except(attributes,i_A), all_except(attr_labels,i_A)))
    return root


def all_except(l, i):
    return l[:i]+l[(i+1):]

def most_common(l):
    return max(set(l), key=l.count)


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
    dt = ID3(examples, attributes, range(0,len(attributes)))
    save_dt(dt, dt_fn) #Save the decision tree
    print "Built decision tree for "+train_data_fn+" saved in "+dt_fn


#Build decision tree from passed file
build_decision_tree(sys.argv[1], sys.argv[2])


