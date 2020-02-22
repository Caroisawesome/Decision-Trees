import math
import numpy as np

# data = a row of data containing counts [ AN, AIE, AEI, TN, ... GN, ... , CN, ... ]
# imp : { 0, 1, 2 } where 0 calculates entropy, 1 calculates gini index, and 2 missclassificationError
def information_gain(data, imp):

    # [ P_N, P_IE, P_EI]
    P_outcomes = get_outcome_probabilities(data)

    # [ P_A, P_ T, P_G, P_C ]
    P_nucleotides = get_nucleotide_probabilities(data)

    # [ P_AN, P_AIE, P_AEI, P_TN, P_TIE, P_TIE, P_GN,... P_CN, ...]
    P_nucl_outcome = get_nucleotide_outcome_probabilities(data)

    if (imp == 0):
        HD = entropy(P_outcomes)
        for i in range(0,4):
            index = i * 3
            HDA = entropy([P_nucl_outcome[index], P_nucl_outcome[index+1],P_nucl_outcome[index+2]])
            HD -= P_nucleotides[i]*HDA
        return HD

    elif(imp ==1):
        # TODO!
        print("need to do gini index")
        return 0
    else:
        # TODO!
        print("need to do missclassificationError")
        return 0


# Get the probability of each (nucleotide, outcome) pair
# returns an array of 12 probabilities:     # [ P_AN, P_AIE, P_AEI, P_TN, ... , P_GN,... P_CN, ...]
#     where P_AN = totalAN/totalA 
def get_nucleotide_outcome_probabilities(data):

    # total A, Total T, total G, total C
    total_nucleotide = np.zeros(4)

    # probabilities e.g. (A,N)/totalN,  (T,EI)/TotalEI
    prob_nucl_outcomes = np.zeros(12)

    for i in range(0,4):
        index = i*3
        total_nucl = data[index] + data[index+1] + data[index+2]
        total_nucleotide[i] = total_nucl

        for j in range(0,3):
            if (total_nucl > 0):
                prob_nucl_outcomes[index+j] = data[index+j]/total_nucl
            else:
                prob_nucl_outcomes[index+j] = 0

    return prob_nucl_outcomes

# Get the probability of each nucleotide in the data
#      returns an array [ P_A, P_ T, P_G, P_C ]
#      where P_A = totalA/total 
def get_nucleotide_probabilities(data):
    total=0
    # total A, Total T, total G, total C
    total_nucleotide = np.zeros(4)

    for i in range(0,4):
        index = i*3
        total_nucleotide[i] = data[index] + data[index+1] + data[index+2]
        total += total_nucleotide[i]

    prob_each_nucleotide = [x/total for x in total_nucleotide]
    return prob_each_nucleotide

# Get the probability of each outcome in the data.
#      returns an array [P_N, P_IE, P_EI]
#      where P_N = TotalN/Total, etc.
def get_outcome_probabilities(data):

    total_each_outcome = np.zeros(3)
    for i in range(0,3):
        total_each_outcome[i] = (data[i] + data[i+3] + data[i+6] + data[i+9])

    total = sum(total_each_outcome)

    # probabilities e.g. totalN/total,  totalIE/total, TotalEI/total
    prob_each_outcome = [x / total for x in total_each_outcome]
    return prob_each_outcome


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


# data: array of probabilities 
def entropy(data):
    ent = 0
    for p in data:
        if (p != 0):
            ent += -1 * p * (math.log(p))
    return ent

# data: array of probabilities ?
def gini_index(data):

    sum = 0;
    for p in data:
        sum += p ** 2

    return 1 - sum

