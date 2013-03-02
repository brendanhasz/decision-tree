# build_dt.py
# Builds a decision tree from a file

import pickle


def build_dt(filename):

def save_dt(dt, filename):
    thefile = open(filename, 'w')
    pickle.dump(dt, thefile)
    thefile.close()

def load_dt(filename):
    thefile = open(filename, 'r')
    dt = pickle.load(thefile)
    return dt

