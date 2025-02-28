from scipy.stats import chi2
import random as rnd

import math
import tree
import impurity
import data
import sys


def classify_data(t, p1, p2):
    """

    Non recursive function wich takes a decision tree and two parameters. The two parameters
    are used to name the new output file, and the tree is used to classify a new data set.

    """
    testing = data.read_test_csv('testing.csv')
    dat    = []
    for x in testing:
        dat.append((x[0], classify(x[1], t)))
    data.write_csv(dat, (str(p1) + str(p2)))

def classify(line, t):
    """

    Recursive function which takes a line of data, ATCGG..., a decision tree, and recursively
    scans the tree to classify the new piece of data as EI, IE, or N. Upon finding any of the
    characters N, D, S, or R, a random value that it corresponds to is then chosen.

    """
    idx = t.label
    # A, T, G, C are chosen at random for a given value of N, D, S, or R.
    N   = ['A', 'T', 'G', 'C']
    D   = ['A', 'T', 'G']
    S   = ['C', 'G']
    R   = ['A', 'G']
    r   = 0

    if idx < 0:
        return t.classification
    else:
        val = line[idx]

    if val == 'N':
        r = rnd.randrange(3)
        new = N[r]
        val = new
    elif val == 'D':
        r = rnd.randrange(2)
        new = D[r]
        val = new
    elif val == 'S':
        r = rnd.randrange(1)
        new = S[r]
        val = new
    elif val == 'R':
        r = rnd.randrange(1)
        new = R[r]
        val = new

    for c in t.children:
        if c.attr == val:
            return classify(line, c)


def dt_construct(raw, blacklist, parent, attr, confidence_level, impurity_type):
    """

    Find next optimal position to split
    calculate if it is worth splitting on that node
    if yes, then split on that node ( remove that column from the data)
    call d_t contstruct on the remaining data

    """

    d = data.gen_data(raw, blacklist)

    # Create a new node for the tree.
    node = tree.Tree()
    # Get the new position to split for the latest node
    position_to_split = get_root_node(d, blacklist, confidence_level, impurity_type)
    node.children = []
    node.attr = attr

    if position_to_split >= 0:
        node.label = position_to_split

        parent.children.append(node)
        blacklist.append(position_to_split)
        raw_segmented_data = split_data(raw, position_to_split)

        num_segments = len(raw_segmented_data)
        # recursively call dt_construct in order to build the tree.
        for i in range(0,num_segments):
            if i == 0:
                dt_construct(raw_segmented_data[i], blacklist, node, 'A', confidence_level, impurity_type)
            if i == 1:
                dt_construct(raw_segmented_data[i], blacklist, node, 'T',confidence_level, impurity_type)
            if i == 2:
                dt_construct(raw_segmented_data[i], blacklist, node, 'G',confidence_level, impurity_type)
            else:
                dt_construct(raw_segmented_data[i], blacklist, node, 'C',confidence_level, impurity_type)
    else:
        cl = get_classification(raw)
        node.classification = cl
        parent.children.append(node)

def get_classification(data):
    """

    Determine what the classification should be for the remaining data.
    Returns the classification that appears the most in the remaining data.

    """
    counts = [0,0,0] # N, IE, EI
    vals = ['N', 'IE', 'EI']
    for row in data:
        idx = vals.index(row[2])
        counts[idx] += 1
    idx = counts.index(max(counts))
    return vals[idx]


def split_data(raw_data, index):
    """

    Splits the raw data from the csv file, into 4 subsets
    Each row is added to the subset with the matching nucleotide 
    at the given index in the nucleotide string

    """

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


def chi_square(data, index, confidence_level):
    """

    Function for computing the chi squared test over a set of data, takes a set of data,
    a given index, and a chosen confidence level. Is used to determine when to stop splitting
    while building the decision tree.

    """
    classes  = 3
    values   = 4
    prob     = 0.99
    total    = 0
    d        = data[index]
    expected = []

    if confidence_level == 0:
        prob = 0.95
    elif confidence_level == 1:
        prob = 0.99
    else:
        prob = 0

    # Compute all the totals for A, T, G, and C respectively.
    totals   =  [d[0] + d[3] + d[6] + d[ 9], d[1] + d[4] + d[7] + d[10], d[2] + d[5] + d[8] + d[11]]
    a_tot    = d[0] + d[ 1] + d[ 2]
    t_tot    = d[3] + d[ 4] + d[ 5]
    g_tot    = d[6] + d[ 7] + d[ 8]
    c_tot    = d[9] + d[10] + d[11]
    val      = 0

    # Add up total of all values in a given position.
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

    critical = chi2.ppf(prob, (classes - 1) * (values - 1))
    if abs(val) >= critical:
        return True
    else:
        return False

def get_root_node(counts, blacklist, confidence_level, impurity_type):
    """
 
    Takes the set of data as a list of tuples, the blacklist of positions which we are not
    looking at, a confidence level and the impurity type to look at as an integer.
    Returns an integer representing the position

    """
    Ig_old = 0
    position = -1
    for i in range(0,60):
        if i not in blacklist:
            Ig_new = impurity.information_gain(counts[i], impurity_type)

            if Ig_new > Ig_old:
                Ig_old = Ig_new
                position = i

    if (chi_square(counts, position, confidence_level)):
        ## Split again!
        return position
    else:
        ## do not split anymore! Not worth it
        return -1

def print_tree(t):
    """

    Print out our tree as parens, attributes, labels, and classifications.

    """
    print("(" + str(t.attr) + str(t.label) + str(t.classification), end='')
    for i in t.children:
        print_tree(i)
    print(")", end='')


if (__name__ == '__main__'):

    if len(sys.argv) < 3:
        print("Must enter commandline arguments <confidence_level> and <impurity_type>")
        print("confidence_level: 0 -> 95%, 1 -> 99%, 2 -> 0%")
        print("impurity_type: 0 -> Entropy, 1 -> Gini Index, 2 -> Missclassification Error")
        exit(0)

    confidence_level = int(sys.argv[1])
    impurity_type = int(sys.argv[2])

    # reads data from csv, and creates a 60 array of length 12 tuples 
    raw = data.read_csv('training.csv')
    t = tree.Tree()
    t.children = []
    t.label    = 0
    t.attr     = ""
    dt_construct(raw, [], t, "", confidence_level, impurity_type)
    classify_data(t.children[0], confidence_level, impurity_type)
