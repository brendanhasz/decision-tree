# bagdtapply.py
# Applies a bootstrap aggregate model to test data

import sys
from bagdt_utils import *

# Apply bootstrap aggregate model to passed test file
if len(sys.argv)==4:
    print "Applying bootstrap aggregate model in "+sys.argv[2]+" to "+sys.argv[1]
    apply_bagged_dt(sys.argv[1], sys.argv[2], sys.argv[3])
    print "Done. Output saved as "+sys.argv[3]
else:
    print "\nUSAGE: python bagdtapply.py <test_filename> <dcn_tree_filename> <output_filename>\n\n"

