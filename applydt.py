# applydt.py
# Applies a decision tree to a test file and classifies the data

import sys
from dt_io import *
from Tree import *


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
    outstr='\n'.join([[c[i]+','+''.join(att[i])][0] for i in range(0,len(c))])
    thefile = open(filename, 'w')
    thefile.write(outstr+'\n')
    thefile.close()


def most_common(l):
    return max(set(l), key=l.count)


def apply_decision_tree(test_data_fn, dt_fn, output_fn):
    print "Applying decision tree "+dt_fn+" to test file "+test_data_fn+" ..."
    att = parse_test_file(test_data_fn)
    dt = load_dt(dt_fn)
    classes = [classify(a, dt) for a in att] #classify each attr list
    classes = [c if c!=None else most_common(classes) for c in classes] #cleanup
    write_output_file(classes, att, output_fn)
    print "Done! Classified attributes stored in "+output_fn


#Apply decision tree on data in passed file
if len(sys.argv)==4:
    apply_decision_tree(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print "\nUSAGE: python applydt.py <test_data_filename> <dt_filename> <output_filename>\n\n"


