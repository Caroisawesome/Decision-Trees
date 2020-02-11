import math
import numpy as np

def information_gain(data):

    total = 0
    total_nucleotide = (0, 0 ,0,0) # total A, Total T, total G, total C
    prob_nucl_outcomes = np.zeros(12)

    for i in range(0,4):
        index = i*3
        total_nucleotide[i] = data[index] + data[index+1] + data[index+2]
        total += total_nucleotide[i]
        prob_nucl_outcomes[index] = data[index]/total_nucleotide[i]
        prob_nucl_outcomes[index+1] = data[index+1]/total_nucleotide[i]
        prob_nucl_outcomes[index+2] = data[index+2]/total_nucleotide[i]

    

# type: 3integer. 0 to calculate missclassificationError, 1 to calculate entropy, 2 to calculate giniIndex
def impurity(type, data):
    if (type == 0):
        missclassification_error(data)
    elif (type == 1):
        entropy(data)
    else:
        gini_index(data)

def missclassification_error(data):
        return 0


# data: array of probabilities ?
def entropy(data):
    ent = 0
    for p in data:
        ent += -1 * p * (math.log(p))
    return ent

# data: array of probabilities ?
def gini_index(data):

    sum = 0;
    for p in data:
        sum += p ** 2

    return 1 - sum

