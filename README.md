# Decision-Trees-ML

This Decision-Tree-ML repo implements a ID3 decision tree algorithm that was trained using the data from `training.csv`. 

## To run the program:

Install dependencies:
`pip install math`
`pip install pickle`
`pip install numpy`

Run:
`python main.py <confidence_level> <impurity_type>`
`confidence_level`: {0,1,2} - 0: 95%, 1: 99%, 2: 0%
`impurity_type`: {0,1,2} - 0: Entropy, 1: Gini Index, 2: Missclassification Error

## Files:

`main.py` contains the main function that starts the ID3 algorithm. Reads data from `training.csv` and builds up a decision tree.

`impurity.py` contains methods that calculate the information gain, either by calculating the entropy of the data, or by using Gini Index or Missclassification Error.

`data.py` converts the raw data that was imported from the csv, into a data structure containing sums for all the (nucleotide value, classification) combinations in a given position.

`tree.py` contains a tree class that is used to contain the structure of the decision tree.

`training.csv` contains the data that is used to build the decision tree.

`testing.csv` contains the testing data that is used to determine the accuracy of the decision tree.



### Some functions:

Gini_index 

Entropy

Missclassification_error

Impure - calls gini-index or entropy or missclassification-error

Information_gain - call Impure method

chi-square - performs a chi-square test

