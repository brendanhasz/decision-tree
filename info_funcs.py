# info_funcs.py
# Information theory functions (entropy, information gain, etc)

from math import log


def info_gain(Y, A):
    thesum = 0
    for e in set(A):
        Ya = []
        for i in range(0,len(A)):
            if A[i]==e:
                Ya.append(Y[i])
        thesum = thesum + len(Ya)/len(A)*entropy(Ya)
    return entropy(Y)-thesum
        
    
def entropy(Y):
    thesum = 0
    for e in set(Y):
        pyi = len([v for v in Y if v==e])/float(len(Y))
        thesum = thesum + pyi*log(1/pyi,2)
    return thesum


