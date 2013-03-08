# applydt.py
# Applies a decision tree to a test file and classifies the data

from applydt_utils import *

#Apply decision tree on data in passed file
if len(sys.argv)==4:
    apply_decision_tree(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print "\nUSAGE: python applydt.py <test_data_filename> <dt_filename> <output_filename>\n\n"


