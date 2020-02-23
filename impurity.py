import math
import numpy as np

def information_gain(data, imp):
    """

    data = a row of data containing counts [ AN, AIE, AEI, TN, ... GN, ... , CN, ... ]
    imp : { 0, 1, 2 } where 0 calculates entropy, 1 calculates gini index, and 2 
    missclassificationError

    """

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

    elif(imp == 1):
        Imp_D = gini_index(P_outcomes)
        for i in range(0,4):
            index = i * 3
            imp_d_nucl = gini_index([P_nucl_outcome[index], P_nucl_outcome[index+1],P_nucl_outcome[index+2]])
            Imp_D -= P_nucleotides[i]*imp_d_nucl

        return Imp_D

    else:

        Imp_D = miss_error(P_outcomes)
        for i in range(0,4):
            index = i * 3
            imp_d_nucl = miss_error([P_nucl_outcome[index], P_nucl_outcome[index+1],P_nucl_outcome[index+2]])
            Imp_D -= P_nucleotides[i]*imp_d_nucl

        return Imp_D



def get_nucleotide_outcome_probabilities(data):
    """

    Get the probability of each (nucleotide, outcome) pair
    returns an array of 12 probabilities:
    [ P_AN, P_AIE, P_AEI, P_TN, ... , P_GN,... P_CN, ...]
        where P_AN = totalAN/totalA 

    """

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
 
def get_nucleotide_probabilities(data):
    """

    Get the probability of each nucleotide in the data
    returns an array [ P_A, P_ T, P_G, P_C ]
    where P_A = totalA/total

    """
    total=0
    # total A, Total T, total G, total C
    total_nucleotide = np.zeros(4)

    for i in range(0,4):
        index = i*3
        total_nucleotide[i] = data[index] + data[index+1] + data[index+2]
        total += total_nucleotide[i]

    prob_each_nucleotide = [x/total for x in total_nucleotide]
    return prob_each_nucleotide

def get_outcome_probabilities(data):
    """

    Get the probability of each outcome in the data.
    returns an array [P_N, P_IE, P_EI]
    where P_N = TotalN/Total, etc.

    """

    total_each_outcome = np.zeros(3)
    for i in range(0,3):
        total_each_outcome[i] = (data[i] + data[i+3] + data[i+6] + data[i+9])

    total = sum(total_each_outcome)

    # probabilities e.g. totalN/total,  totalIE/total, TotalEI/total
    prob_each_outcome = [x / total for x in total_each_outcome]
    return prob_each_outcome


def miss_error(data):
    """

    Compute misclassification error given data set.

    """
    return 1 - max(data)


def entropy(data):
    """

    Compute entropy given a set of data.

    """
    ent = 0
    for p in data:
        if (p != 0):
            ent += -1 * p * (math.log(p))
    return ent

def gini_index(p_outcomes):
    """

    Compute gini index given p outcomes.

    """
    sum = 0
    for i in range(0, len(p_outcomes)):
        sum += p_outcomes[i]**2
    return 1 - sum
