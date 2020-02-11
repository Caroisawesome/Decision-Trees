import tree
import impurity
import pickle
import data



def dt_construct(d,t):
    return 0
        # find Root node
        # calculate if it is worth splitting on that node
        # if yes, then split on that node ( remove that column from the data),
        #         call d_t contstruct on the remaining data
    #split_on_position = get_position_with_greatest_information_gain(d)

    # t.data = representative_class(d) 
    # if impure(d):
    #     criterion = split_criterion(d)
    # else: 
    #     return t
    # D = decompose(d, criterion)
    # for d_val in D:
    #     add_successor(t, dt_construct(d_val,t))
    # return ti

def get_position_with_greatest_information_gain(counts):

    # Constant, decides when to stop splitting
    split_criterion = 0.05

    Ig_old = 0
    position = -1
    for i in range(0,60):
        Ig_new = information_gain(counts[i])

        if Ig_new > Ig_old:
            Ig_old = Ig_new
            position = i

    if (Ig_old < split_criterion):
        ## do not split anymore! Not worth it
        return -1
    else:
        return position


if (__name__ == '__main__'):
#def __main__():

    # reads data from csv, and creates a 60 array of length 12 tuples 
    d = data.gen_dat()#  read data from csv
    print(d)
    t = Tree()
    t = dt_construct(d,t)

    file = open('decision_tree',  'wb')
    pickle.dump(t, file)
    file.close()
