import math

# type: integer. 0 to calculate missclassificationError, 1 to calculate entropy, 2 to calculate giniIndex
def impurity(type, data):
    if (type == 0):
        missclassificationError(data)
    elif (type == 1):
        entropy(data)
    else:
        giniIndex(data)

def missclassificationError(data):
        return 0


# data: array of probabilities ?
def entropy(data):
    ent = 0
    for p in data:
        ent += -1 * p * (math.log(p))
    return ent

# data: array of probabilities ?
def giniIndex(data):

    sum = 0;
    for p in data:
        sum += p ** 2

    return 1 - sum

