import csv
import random

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

    r   = 0
    an  = 0
    aie = 0
    aei = 0

    gn  = 0
    gie = 0
    gei = 0

    cn  = 0
    cie = 0
    cei = 0

    tn  = 0
    tie = 0
    tei = 0

    for i in range(0, 60):
        # NOTE: removed for testing purposes!
        # but, after further consideration, we might not need to blacklist these after all?
        #if i in blacklist:
        #    continue
        for dat in x:
            #print(dat[1][i])
            if   dat[1][i] == 'A':
                if   dat[2] == "N":
                    an += 1
                elif dat[2] == "IE":
                    aie += 1
                elif dat[2] == "EI":
                    aei += 1

            elif dat[1][i] == 'T':
                if   dat[2] == "N":
                    tn += 1
                elif dat[2] == "IE":
                    tie += 1
                elif dat[2] == "EI":
                    tei += 1

            elif dat[1][i] == 'G':
                if   dat[2] == "N":
                    gn += 1
                elif dat[2] == "IE":
                    gie += 1
                elif dat[2] == "EI":
                    gei += 1

            elif dat[1][i] == 'C':
                if   dat[2] == "N":
                    cn += 1
                elif dat[2] == "IE":
                    cie += 1
                elif dat[2] == "EI":
                    cei += 1

            elif dat[1][i] == 'D' or dat[1][i] == 'N' or dat[1][i] == 'S' or dat[1][i] == 'R':
                r = random.randrange(3)
                if r == 0:
                    if   dat[2] == "N":
                        an += 1
                    elif dat[2] == "IE":
                        aie += 1
                    elif dat[2] == "EI":
                        aei += 1
                if r == 1:
                    if   dat[2] == "N":
                        tn += 1
                    elif dat[2] == "IE":
                        tie += 1
                    elif dat[2] == "EI":
                        tei += 1



        #print(str(an) + ", " + str(aie) + ", " + str(aei) + ", " + str(tn) + ", " + str(tie) + ", " + str(tei) + ", " + str(gn) + ", " + str(gie) + ", " + str(gei) + ", " + str(cn) + ", " + str(cie) + ", " + str(cei))

        out.append((an, aie, aei, tn, tie, tei, gn, gie, gei, cn, cie, cei))
        an  = 0
        aie = 0
        aei = 0

        gn  = 0
        gie = 0
        gei = 0

        cn  = 0
        cie = 0
        cei = 0

        tn  = 0
        tie = 0
        tei = 0

    return out
