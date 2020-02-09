import Tree
import impurity
import pickle

def main():

        # d is an array of tuples containing an id, DNA values, and the final classification
    d = [()]#  read data from csv
    t = Tree()
    t = dt_construct(d,t)

    file = open('decision_tree',  'wb')
    pickle.dump(t, file)
    file.close()


def dt_construct(d,t):

        # find Root node
        # calculate if it is worth splitting on that node
        # if yes, then split on that node ( remove that column from the data),
        #         call d_t contstruct on the remaining data

    t.data = representative_class(d) 
    if impure(d):
        criterion = split_criterion(d)
    else: 
        return t
    D = decompose(d, criterion)
    for d_val in D:
        add_successor(t, dt_construct(d_val,t))
    return t
