#!/usr/bin/env python
class Tree(object):
    """

    Tree object used for decision trees.

    """
    def __init__(self):
        self.children = None
        self.label    = -1
        self.attr     = None
        self.classification = None

