import Tree
import Impurity
import pickle

def main():
	d = []#  read data from csv

	t = dt_construct(d)

	## Then pickle tree
	## dump pickled tree into file 
	file = open('decision_tree',  'wb')
	pickle.dump(t, file)
	file.close()


def dt_construct(d):
    t = Tree()

    t.data = representative_class(d) 
    if impure(d):
        criterion = split_criterion(d)
    else: 
        return t
    D = decompose(d, criterion)
    for d_val in D:
        add_successor(t, dt_construct(d_val))
    return t
