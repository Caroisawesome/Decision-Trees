# Decision-Trees-ML

This Decision-Tree-ML repo implements a ID3 decision tree algorithm that was trained using the data from `training.csv`. 

## To run the program:

Install dependencies:
`pip install math`
`pip install pickle`
`pip install numpy`

Run:
`python main.py`


## Files:

`main.py` contains the main function that starts the ID3 algorithm. Reads data from `training.csv` and builds up a decision tree.

`impurity.py` contains methods that calculate the information gain, either by calculating the entropy of the data, or by using Gini Index or Missclassification Error.

### Some functions:

Gini_index 

Entropy

Missclassification_error

Impure - calls gini-index or entropy or missclassification-error

Information_gain - call Impure method

chi-square - performs a chi-square test

