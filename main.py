import Tree
import Impurity


def main():
	d = []#  read data from csv

	t = dtConstruct(d)

	## Then pickle tree
	## dump pickled tree into file 



def dtConstruct(d):
    t = Tree()

    t.data = representativeClass(d) 
    if impure(d):
        criterion = splitCriterion(d)
    else: 
        return t
    D = decompose(d, criterion)
    for dVal in D:
        addSuccessor(t, dtConstruct(dVal))
    return t
