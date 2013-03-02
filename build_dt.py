# build_dt.py
# Builds a decision tree from a file

import pickle
import sys


build_decision_tree(sys.argv[1]) #Build decision tree from passed file


def build_decision_tree(filename):
    return filename


def save_dt(dt, filename):
    thefile = open(filename, 'w')
    pickle.dump(dt, thefile)
    thefile.close()


def load_dt(filename):
    thefile = open(filename, 'r')
    dt = pickle.load(thefile)
    return dt

