# dt_io.py
# Functions to save and load decision trees to file

import pickle

def save_dt(dt, filename):
    thefile = open(filename, 'w')
    pickle.dump(dt, thefile)
    thefile.close()


def load_dt(filename):
    thefile = open(filename, 'r')
    dt = pickle.load(thefile)
    return dt

