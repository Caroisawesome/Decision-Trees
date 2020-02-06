import Tree
import Impurity


def main():
	d = []#  read data from csv

	t = dt_construct(d)

	## Then pickle tree
	## dump pickled tree into file 



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
