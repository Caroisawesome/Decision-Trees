import pickle

def print_tree(t):
    print("(" + str(t.attr) + str(t.label), end='')
    for i in t.children:
        print_tree(i)
    print(")", end='')


with open('decision_tree', 'rb') as data_file:
    dt = pickle.load(data_file)

print("PICKLEDATA", 'r')
print(print_tree(dt))
