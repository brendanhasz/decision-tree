# dt_utils.py
# Utility functions for decicion tree programs

import sys
from Tree import *

#Global variables
MAX_RECURSION = 15 #Max depth of the tree
perc_train = 0.8 #percent of training samples to use for making this tree


###################################################
# Information theory functions (entropy, information gain, etc)
from math import log

def info_gain(Y, A):
    thesum = 0
    #print "lenY="+str(len(Y))+"   lenA="+str(len(A))
    for e in set(A):
        Ya = []
        for i in range(0,len(Y)):
            if A[i]==e:
                Ya.append(Y[i])
        thesum = thesum + float(len(Ya))/len(A)*entropy(Ya)
    return entropy(Y)-thesum
        
    
def entropy(Y):
    thesum = 0
    for e in set(Y):
        pyi = len([v for v in Y if v==e])/float(len(Y))
        thesum = thesum + pyi*log(1/pyi,2)
    return thesum
    

###################################################
# Input/Output functions -save and load decision trees to file
import pickle

def save_dt(dt, filename):
    thefile = open(filename, 'w')
    pickle.dump(dt, thefile)
    thefile.close()


def load_dt(filename):
    thefile = open(filename, 'r')
    dt = pickle.load(thefile)
    return dt


###################################################
# Builder functions
def all_except(l, i):
    return l[:i]+l[(i+1):]


def most_common(l):
    return max(set(l), key=l.count)


def ID3(ex, att, attr_labels, rl):
    '''
    Performs the Interactive Dichotomiser 3 algorithm on a list of examples
    and a list of lists of attributes.  attr_labels is the list of labels
    for the attributes, and rl is the recursion level
    '''
    root = Tree()
    print rl
    if rl>MAX_RECURSION: #Upon max recursion, return most frequent
        root.data = most_common(ex)
        return root
    if len(set(ex))==1: #if only 1 class of ie left, use it
        root.data = ex[0]
    elif len(att)<1: #if no attributes left, use most common
        root.data = most_common(ex)
    else:
        #Find attribute that best classifies examples
        maxinfo = 0
        i_A = -1
        for i in range(0,len(att)):
            thisinfo = info_gain(ex, att[i])
            if thisinfo>maxinfo:
                i_A = i
                maxinfo=thisinfo
        if i_A>=0:
            root.data = attr_labels[i_A] #Store node attribute label
            A = att[i_A]
        else: #no class has any more info than any other
            root.data = attr_labels[0]
            A = att[0]
        #For each possible value of max info attribute, add branch
        for v in set(A):
            child = Tree()
            child.data = v
            root.addchild(child)
            #Take 'used' elements out of ex and att!
            E_v = []
            att_v = [[] for i in range(0,len(att))]
            for i in range(0,len(A)):
                if A[i]==v:
                    E_v.append(ex[i])
                    [att_v[j].append(att[j][i]) for j in range(0,len(att))]
            if len(E_v)<1:
                leaf = Tree()
                leaf.data = most_common(ex)
                child.addchild(leaf)
            else:
                 child.addchild(ID3(E_v, all_except(att_v,i_A), all_except(attr_labels,i_A), rl+1))
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
    dt = ID3(examples, attributes, range(0,len(attributes)),1)
    save_dt(dt, dt_fn) #Save the decision tree
    print "Built decision tree for "+train_data_fn+" saved in "+dt_fn


###################################################
# Classifier functions
def classify(att, dt):
    '''
    Classify a single set of attributes, given a decision tree
    '''
    if dt.isleaf(): #dt is decision node
        if dt.data==None:
            return str(2)
        else:
            return str(dt.data)
    else: #dt is attr label node w/ possible attr children
        for c in dt.children:
            if c.data==att[dt.data]: ##this child is the corresponding attribute
                return classify(att, c.children[0])


def parse_test_file(filename):
    '''
    Parses a test file of comma-separated attributes into a list of
     lists of attributes
    '''
    data = []
    thefile = open(filename, 'r')
    [data.append(l.strip().split(',')) for l in thefile]
    thefile.close()
    return data


def write_output_file(c, att, filename):
    '''
    Writes classes and attributes to file filename
    '''
    outstr='\n'.join([[c[i]+','+','.join(att[i])][0] for i in range(0,len(c))])
    thefile = open(filename, 'w')
    thefile.write(outstr+'\n')
    thefile.close()


def apply_decision_tree(test_data_fn, dt_fn, output_fn):
    print "Applying decision tree "+dt_fn+" to test file "+test_data_fn+" ..."
    att = parse_test_file(test_data_fn)
    dt = load_dt(dt_fn)
    classes = [classify(a, dt) for a in att] #classify each attr list
    classes = [c if c!=None else most_common(classes) for c in classes] #cleanup
    write_output_file(classes, att, output_fn)
    print "Done! Classified attributes stored in "+output_fn
    
    
###################################################
# Bagging - utilities for Bootstrap aggregation model
from random import randrange

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



