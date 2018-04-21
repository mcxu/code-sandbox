'''
Created on Apr 11, 2018

@author: MichaelXu

Decision tree classifier written from scratch using CART 
(Classification and Regression Trees) algorithm.
tutorial: https://www.youtube.com/watch?v=LDRbO9a6XPU
github: https://github.com/random-forests/tutorials/blob/master/decision_tree.ipynb
'''
from distutils.log import info

# Note in this example, left node/leaf is true, right node/leaf is false.
# dataset
training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon']]

# column labels
header = ["color", "diameter", "label"]

def unique_vals(rows, col):
    """Find the unique values for a column in a dataset."""
    value_list = [row[col] for row in rows]
    #print("unique_vals:value_list: ", value_list)
    return set(value_list)

def test_unique_vals():
    for col_index in range(len(training_data[0])):
        result = unique_vals(training_data, col_index)
        print("unique vals for col {}: {}".format(col_index, result))

def class_counts(rows):
    """ Counts occurrences of each type in a dataset """
    counts = {}
    for row in rows:
        label  = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

def test_class_counts():
    result = class_counts(training_data)
    print("test_class_counts:result: ", result) # result:  {'Apple': 2, 'Grape': 2, 'Lemon': 1}

def is_numeric(value):
    is_num = isinstance(value, int) or isinstance(value, float)
    return is_num

def test_is_numeric():
    test_list = [1,2,3,"a","b","c",1.12,2.23,3.34]
    for item in test_list:
        result = is_numeric(item)
        print("is_numeric:tested_item: {} is numeric: {}".format(item, result))

def partition(rows, question):
    """ partitions a dataset. """
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return (true_rows, false_rows)

def calculate_gini_impurity(rows):
    """ calculate gini impurity for a list of rows. 
    from: https://en.wikipedia.org/wiki/Decision_tree_learning#Gini_impurity
    @param rows: the input dataset. 
    """
    counts = class_counts(rows)
    print("calculate_gini_impurity:counts: ", counts)
    impurity = 1
    for label in counts:
        print("calculate_gini_impurity:found label: ", label)
        prob_of_label = counts[label] / float(len(rows))
        impurity -= prob_of_label**2
    return impurity

def test_calc_gini_impurity():
    no_mixing = [['Apple'],
                ['Apple']]
    result = calculate_gini_impurity(no_mixing)
    print("gini impurity no mixing: ", result)
    
    some_mixing = [['Apple'],
                   ['Orange']]
    result = calculate_gini_impurity(some_mixing)
    print("gini impurity some mixing: ", result)
    
    result = calculate_gini_impurity(training_data)
    print("gini impurity: ", result)

def calculate_info_gain(left, right, current_uncertainty):
    """ Information gain. The uncertainty of the starting node minus
    weighted impurity of two child nodes.
    """
    print("entered calculate_info_gain")
    p = float(len(left)) / (len(left) + len(right))
    print("calculate_info_gain:p: ", p)
    print("calculate_info_gain:calculating left info gain")
    a = p*calculate_gini_impurity(left)
    print("calculate_info_gain:calculating right info gain")
    b = (1-p)*calculate_gini_impurity(right)
    info_gain = current_uncertainty - a - b
    print("calculate_info_gain:calcd info_gain: ", info_gain)
    return info_gain

def test_calc_info_gain():
    # calculate uncertainty of training data
    current_uncertainty = calculate_gini_impurity(training_data)
    
    # how much info do we gain by partitioning on Green?
    (true_rows, false_rows) = partition(training_data, Question(0,"Green"))
    print("true_rows: ", true_rows)
    print("false_rows: ", false_rows)
    info_gain = calculate_info_gain(true_rows, false_rows, current_uncertainty)
    print("info gain from partitioning on green: ", info_gain)

def find_best_split(rows):
    """ Find the best question to aks by iterating over every feature/value
    and calculating the information gain.
    """
    print("find_best_split:rows: ", rows)
    best_gain = 0 # keep track of best information gain
    best_question = None # keep track of the feature/value that produced it.
    current_uncertainty = calculate_gini_impurity(rows)
    n_features = len(rows[0]) - 1 # column index
    print("find_best_split:n_features: ", n_features)
    
    print("find_best_split:right before outer for loop")
    for col in range(n_features):
        print("find_best_split:entered outer for loop")
        print("find_best_split:col: ", col)
        values = set(row[col] for row in rows) # unique values in column
        print("find_best_split:unique column values: ", values)
        
        for val in values:
            print("find_best_split:entered inner for loop")
            print("find_best_split:val: ", val)
            question = Question(col, val)
            print("find_best_split:Question to test!!!!!: ", question)
            
            # try splitting dataset
            (true_rows, false_rows) = partition(rows, question)
            
            # skip this split if it doesn't divide the dataset
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue
            
            # calculate the information gain from this split
            print("find_best_split:true_rows: ", true_rows)
            print("find_best_split:false_rows: ", false_rows)
            gain = calculate_info_gain(true_rows, false_rows, current_uncertainty)
            
            if gain >= best_gain:
                best_gain = gain
                best_question = question
                
    return (best_gain, best_question)

def test_find_best_split():
    (best_gain, best_question) = find_best_split(training_data)
    print("test_find_best_split:best_gain: ", best_gain)
    print("test_find_best_split:best_question: ", best_question)  


class Question:
    """ Used to partition a dataset """
    
    def __init__(self, column, value):
        self.column = column
        self.value = value
    
    def match(self, example):
        # compare the feature value in an example to the feature value in this question
        val = example[self.column]
        print("match:val: ", val, "    self.value: ", self.value)
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value
    
    def __repr__(self):
        # helper method to print question. called every time object of this type is created.
        condition = "=="
        if is_numeric(self.value):
            condition = ">="
            
        # header: 0 = color, 1 = diameter, 2 = label
        return "Is %s %s %s" % (header[self.column], condition, str(self.value))

def test_question_creation():
    print(Question(0,3))
    print(Question(1,4))
    print(Question(2,"asdf"))
    print(Question(0, "Green"))


class Leaf:
    """ A leaf node classifies data. Holds dict of class "fruit" -> number of times
    if appears in the rows from the training data that reach this leaf. 
    """
    
    def __init__(self, rows):
        self.predictions = class_counts(rows)

class Decision_Node:
    """ A decision node asks a question. This holds a reference to the question
    and to the two child nodes.
    """
    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

def build_tree(rows):
    """ Builds the tree.
    """
    print("entered build_tree")
    # Try partitioning dataset on each of the unique attributes.
    # Calc info gain, return question that produces highest gain.
    (gain, question) = find_best_split(rows)
    
    # base case: no info gain. Return a leaf
    if gain==0:
        return Leaf(rows)
    
    # useful feature/value detected here.
    (true_rows, false_rows) = partition(rows, question)
    
    # recursively build the tree branch
    true_branch = build_tree(true_rows)
    false_branch = build_tree(false_rows)
    
    # return a question (which is in a Decision Node).
    # this records the best feature / value to ask at this point, as well
    # as branches to follow.
    return Decision_Node(question, true_branch, false_branch)
    
def print_tree(node, spacing=""):
    print("entered print_tree")
    
    # base case: reach a leaf.
    if isinstance(node, Leaf):
        print(spacing + "Predict: ", node.predictions)
        return
    
    # print the question at this node
    print(spacing + str(node.question))
    
    # call this function recursively on the true branch
    print(spacing + "--> True:")
    print_tree(node.true_branch, spacing="  ")
    
    # call this function recursively on the false branch
    print(spacing + "--> False:")
    print_tree(node.false_branch, spacing="  ")
    
def classify(row, node):
    # base case: reached leaf
    if isinstance(node, Leaf):
        print("classify:returning node.predictions: ", node.predictions)
        return node.predictions
    
    # decide weather to follow true-branch or false branch
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)
    
def test_classify():
    """ The tree predicts 1st row of training data: {fruit, confidence} """
    # build the tree from the training data
    decision_tree = build_tree(training_data)
    #print_tree(decision_tree)
    
    for row in training_data:
        classification = classify(row, decision_tree)
        print("test_classify:classification for {} is: {}".format(row, classification))

def print_leaf(counts):
    total = sum(counts.values()) * 1.0
    probs = {}
    for label in counts.keys():
        probs[label] = str(int(counts[label] / total * 100)) + "%"
    return probs

def test_print_leaf():
    my_tree = build_tree(training_data)
    
    for row in training_data:
        print("test_print_leaf:row: ", row)
        classification = classify(row, my_tree)
        print("test_print_leaf:classification: ", classification)
        probs = print_leaf(classification)
        print("test_print_leaf:prob: ", probs)

testing_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 4, 'Apple'],
    ['Red', 2, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon']]

def evaluate_test_data():
    my_tree = build_tree(training_data)
    for row in testing_data:
        print("Actual: %s. Predicted: %s" % (row[-1], print_leaf(classify(row, my_tree))))

def main():
    #test_calc_gini_impurity()
    #test_calc_info_gain()
    #test_calc_best_split()
    #test_classify()
    #test_print_leaf()
    evaluate_test_data()

if __name__ == "__main__":
    main()
        
    