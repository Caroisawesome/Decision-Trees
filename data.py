import csv

def read_csv(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append((row[0], row[1], row[2]))
    #for d in data:
    #    print(d)
    return data

def gen_dat():
    out = []

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

    x = read_csv('training.csv')

    for i in range(0, 60):
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
