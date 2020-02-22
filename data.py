import csv
import numpy as np
import random as rnd

def read_csv(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append((row[0], row[1], row[2]))
    #for d in data: #    print(d)
    return data

def write_csv(data):
    file = 'output.csv'
    with open(file, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        writer.writerow(['id', 'class'])
        for x in data:
            writer.writerow(x)

def read_test_csv(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append((row[0], row[1]))
    #for d in data: #    print(d)
    return data

def gen_data(x, blacklist):
    out = []

    for i in range(0, 60):
        # NOTE: removed for testing purposes!
        # but, after further consideration, we might not need to blacklist these after all?
        #if i in blacklist:
        #    continue
        sums = np.zeros((3,4))

        for dat in x:
            nucl    = ['A', 'T', 'G', 'C']
            N       = ['A', 'T', 'G', 'C']
            D       = ['A', 'T', 'G']
            S       = ['C', 'G']
            R       = ['A', 'G']
            classes = ['N', 'IE', 'EI']
            val = dat[1][i] # A, T, G, C
            clss = dat[2] # N, IE , EI

            if val != 'N' and val != 'D' and val != 'S' and val != 'R':
                idx_val = nucl.index(val)
                idx_cls = classes.index(clss)
                sums[idx_cls][idx_val] += 1
            elif val == 'N':
                r = rnd.randrange(3)
                idx_cls = classes.index(clss)
                sums[idx_cls][r] += 1
            elif val == 'D':
                r = rnd.randrange(2)
                idx_cls = classes.index(clss)
                sums[idx_cls][r] += 1
            elif val == 'S':
                r = rnd.randrange(2,3)
                idx_cls = classes.index(clss)
                sums[idx_cls][r] += 1
            elif val == 'R':
                r = rnd.randrange(2)
                if r == 0:
                    r = 0
                else:
                    r = 2
                idx_cls = classes.index(clss)
                sums[idx_cls][r] += 1
                

        out.append((sums[0][0], sums[1][0], sums[2][0], sums[0][1], sums[1][1], sums[2][1], sums[0][2], sums[1][2], sums[2][2], sums[0][3], sums[1][3], sums[2][3]))

    return out
