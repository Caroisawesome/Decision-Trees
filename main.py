import tree
import impurity
import pickle
import data



def dt_construct(d,t):

    # calculate if it is worth splitting on that node
    # if yes, then split on that node ( remove that column from the data)
    #         call d_t contstruct on the remaining data

    # find Root node
    position_to_split = get_root_node(d)
    print("Posistion to split", position_to_split)

# returns an integer representing the position
def get_root_node(counts):

    # TODO: use chi square test!
    # Constant, decides when to stop splitting
    split_criterion = 0.05

    Ig_old = 0
    position = -1
    for i in range(0,60):
        Ig_new = impurity.information_gain(counts[i],0)

        if Ig_new > Ig_old:
            Ig_old = Ig_new
            position = i

    if (Ig_old < split_criterion):
        ## do not split anymore! Not worth it
        return -1
    else:
        return position


if (__name__ == '__main__'):

    # reads data from csv, and creates a 60 array of length 12 tuples 
    d = data.gen_dat()#  read data from csv
    t = tree.Tree()
    t = dt_construct(d,t)

    file = open('decision_tree',  'wb')
    pickle.dump(t, file)
    file.close()
