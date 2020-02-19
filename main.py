from scipy.stats import chi2

import math
import tree
import impurity
import pickle
import data


def dt_construct(raw, blacklist, t):

    d = data.gen_data(raw, blacklist)

    # calculate if it is worth splitting on that node
    # if yes, then split on that node ( remove that column from the data)
    #         call d_t contstruct on the remaining data

    position_to_split = get_root_node(d, blacklist)
    print("Position to split", position_to_split)
    if position_to_split >= 0:

        # TODO! add node to tree?
        blacklist.append(position_to_split)
        raw_segmented_data = split_data(raw, position_to_split)

        num_segments = len(raw_segmented_data)
        for i in range(0,num_segments):
            dt_construct(raw_segmented_data[i], blacklist, t)

def split_data(raw_data, index):

    a_dat = []
    t_dat = []
    g_dat = []
    c_dat = []

    vals = ['A', 'T', 'G', 'C']
    data_subsets = [a_dat, t_dat, g_dat, c_dat]

    for row in raw_data:
        d = row[1]
        value_at_index = d[index]
        if value_at_index in vals:
            idx = vals.index(value_at_index)
            data_subsets[idx].append(row)

    return data_subsets


def chi_square(data, index):
    #stat, p, dof, expected = chi2_contigency(data)
    classes  = 3
    values   = 4
    prob     = 0.95
    total    = 0
    d        = data[index]
    expected = []
    # totals[0] = n, totals[1] = ie, totals[2] = ei
    totals   =  [d[0] + d[3] + d[6] + d[ 9], d[1] + d[4] + d[7] + d[10], d[2] + d[5] + d[8] + d[11]]
    a_tot    = d[0] + d[ 1] + d[ 2]
    t_tot    = d[3] + d[ 4] + d[ 5]
    g_tot    = d[6] + d[ 7] + d[ 8]
    c_tot    = d[9] + d[10] + d[11]
    val      = 0

    for i in range(0, len(data[index])):
        total += d[i]

    if total == 0:
        return False

    for j in range(0, len(d)):
        if j < 3:
            expected.append(a_tot * (totals[j % 3] / total))
        elif j >= 3 and j < 6:
            expected.append(t_tot * (totals[j % 3] / total))
        elif j >= 6 and j < 9:
            expected.append(g_tot * (totals[j % 3] / total))
        else:
            expected.append(c_tot * (totals[j % 3] / total))

    for k in range(0, len(d)):
        # what to do if expected is 0???
        if (expected[k] != 0):
            val += ((d[k] - expected[k]) ** 2) / expected[k]

    critical = chi2.ppf(1 - prob, (classes - 1) * (values - 1))
    if abs(val) >= critical:
        return True
    else:
        return False

# returns an integer representing the position
def get_root_node(counts, blacklist):
    print("blacklist", blacklist)
    Ig_old = 0
    position = -1
    for i in range(0,60):
        if i not in blacklist:
            Ig_new = impurity.information_gain(counts[i], 0)

            if Ig_new > Ig_old:
                Ig_old = Ig_new
                position = i

    if (chi_square(counts, position)):
        ## Split again!
        return position
    else:
        ## do not split anymore! Not worth it
        return -1


if (__name__ == '__main__'):

    # reads data from csv, and creates a 60 array of length 12 tuples 
    raw = data.read_csv('training.csv')
    t = tree.Tree()
    t = dt_construct(raw, [], t)

    file = open('decision_tree',  'wb')
    pickle.dump(t, file)
    file.close()
