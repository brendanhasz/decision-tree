# builddt.py
# Builds a decision tree from a file

import sys
from dt_utils import build_decision_tree
DEF_MAX_RECURSION = 10

#Build decision tree from passed file
if len(sys.argv)==3:
    build_decision_tree(sys.argv[1], sys.argv[2], DEF_MAX_RECURSION)
elif len(sys.argv)==4:
    build_decision_tree(sys.argv[1], sys.argv[2], int(sys.argv[3]))
else:
    print "\nUSAGE: python builddt.py <training_data_filename> <dcn_tree_filename> <max_num_recursion>\n\n"

