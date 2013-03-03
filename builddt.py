# builddt.py
# Builds a decision tree from a file

import sys
from dt_io import *
from Tree import *
from info_funcs import *


def ID3(ex, att, attr_labels):
    '''
    Performs the Interactive Dichotomiser 3 algorithm on a list of examples
    and a list of lists of attributes
    '''
    root = Tree()
    if len(set(ex))==1: #if only 1 class of ie left, use it
        root.data = ex[0]
    elif len(att)<1: #if no attributes left, use most common
        root.data = most_common(ex)
    else:
        #Find attribute that best classifies examples
        maxinfo = 0
        print ' '
        for i in range(0,len(att)):
            print len(att)
            print i
            thisinfo = info_gain(ex, att[i])
            if thisinfo>maxinfo:
                i_A = i
                maxinfo=thisinfo
        root.data = attr_labels[i_A] #Store node attribute label
        A = att[i_A]
        #For each possible value of max info attribute, add branch
        for v in set(A):
            child = Tree()
            child.data = v
            root.addchild(child)
            E_v = [ex[i] for i in range(0,len(A)) if A[i]==v]
            #TODO: you also need to take these elements out of att!
            if len(E_v)<1:
                leaf = Tree()
                leaf.data = most_common(ex)
                child.addchild(leaf)
            else:
                 child.addchild(ID3(E_v, all_except(att,i_A), all_except(attr_labels,i_A)))
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


