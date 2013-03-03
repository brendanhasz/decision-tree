# Tree.py
# Brendan Hasz
# Basic implementation of a tree

class Tree(object):
    def __init__(self):
        self.children = []
        self.data = None
    def isleaf(self):
        return len(self.children) < 1
