# gene_seq.py
# Brendan Hasz
# Parses a gene sequence file into a file readable by builddt.py

import sys

usage_str = "\nUSAGE: python gene_seq.py <option> <filename_in> <filename_out>\n\n\t-train\tparse a training file into output file\n\t-test\tparse a test file into output file\n"

if len(sys.argv)!=4:
    print usage_str
else:
    opt = sys.argv[1]
    fn_in = sys.argv[2]
    fn_out = sys.argv[3]
    if opt=='-train':
        infile = open(fn_in, 'r')
        outfile = open(fn_out, 'w')
        for l in infile:
            to = [l.strip().split(',')[-1]] #add class to front
            for e in l.strip().split(',')[:-1]:
                if e=='0':
                    to.append('0')
                else:
                    to.append('1')
            outfile.write(','.join(to)+'\n')
        outfile.close()
        infile.close()
    if opt=='-traintotest':
        infile = open(fn_in, 'r')
        outfile = open(fn_out, 'w')
        for l in infile:
            to = []
            for e in l.strip().split(',')[:-1]:
                if e=='0':
                    to.append('0')
                else:
                    to.append('1')
            outfile.write(','.join(to)+'\n')
        outfile.close()
        infile.close()
    elif opt=='-test':
        infile = open(fn_in, 'r')
        outfile = open(fn_out, 'w')
        for l in infile:
            to = []
            for e in l.strip().split(',')[:-1]:
                if e=='0':
                    to.append('0')
                else:
                    to.append('1')
            outfile.write(','.join(to)+'\n')
        outfile.close()
        infile.close()
    else:
        print usage_str


