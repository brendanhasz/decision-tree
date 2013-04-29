# builddt.py
# Builds a decision tree from a file

import sys
from dt_utils import build_decision_tree

#Build decision tree from passed file
if len(sys.argv)==3:
    build_decision_tree(sys.argv[1], sys.argv[2])
else:
    print "\nUSAGE: python builddt.py <training_data_filename> <dcn_tree_filename>\n\n"

