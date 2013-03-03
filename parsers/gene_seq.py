# gene_seq_parse.py
# Brendan Hasz
# Parses a gene sequence file into a file readable by builddt.py

import sys

fn_in = sys.argv[1]
fn_out = sys.argv[2]

infile = open(fn_in, 'r')
outfile = open(fn_out, 'w')
outfile.write("".join([",".join([l.translate(None,',')][0])[0:-2]+'\n' for l in infile]))
outfile.close()
infile.close()


