# validate.py
# takes classified train data + truth train data, calculates accuracy

import sys

usage_str = "\nUSAGE: python validate.py <predicted.data> <truth.data>\n\n"

if len(sys.argv)!=3:
    print usage_str
else:
    fn_pred = sys.argv[1]
    fn_truth = sys.argv[2]
    pred_file = open(fn_pred, 'r')
    truth_file = open(fn_truth, 'r')
    pclasses = [e[0] for e in pred_file] #get list of classes for predicted labels
    tclasses = [e[0] for e in truth_file] #get list of classes for truth labels
    numcorr = 0
    for i in range(0,len(pclasses)):
        if pclasses[i]==tclasses[i]:
            numcorr = numcorr + 1
    perc_corr = 100.0*float(numcorr)/float(len(pclasses))
    print "PERCENT CORRECTLY CLASSIFIED INSTANCES: "+str(perc_corr)

