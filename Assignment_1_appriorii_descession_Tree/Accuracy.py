from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from Assignment_1_appriorii_descession_Tree import Apriori
import numpy as np
import pandas as pd
import time

# Prepare the data
data = pd.read_csv('GroceryStoreDataSet.csv', header=None)
transactions = []
for i in range(len(data)):
    transactions.append(data.values[i, 0].split(','))

# Create the Apriori class
model_apriori = Apriori(transactions, min_support=0.2, min_confidence=0.5)

# Measure the efficiency of generating frequent itemsets
start_time = time.time()
L = model_apriori.generate_L()
end_time = time.time()
efficiency_apriori = end_time - start_time
print("Apriori Efficiency (Frequent Itemsets):", efficiency_apriori)

# Prepare the dataset for classification
X = []
y = []
for transaction in transactions:
    row = [1 if item in transaction else 0 for itemset in L for item in itemset]
    X.append(row)
    y.append(1)  # We assume all transactions are positive examples

# Split the dataset into training and testing sets for Apriori
X_train_apriori, X_test_apriori, y_train_apriori, y_test_apriori = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the decision tree classifier for Apriori
clf_apriori = DecisionTreeClassifier()
clf_apriori.fit(X_train_apriori, y_train_apriori)

# Make predictions on the testing set for Apriori
y_pred_apriori = clf_apriori.predict(X_test_apriori)

# Calculate the accuracy of the classifier for Apriori
accuracy_apriori = accuracy_score(y_test_apriori, y_pred_apriori)
print("Apriori Accuracy:", accuracy_apriori)

# Prepare the dataset for classification for Decision Tree
X_train_tree, X_test_tree, y_train_tree, y_test_tree = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Measure the efficiency of training the decision tree classifier
start_time = time.time()
clf_tree = DecisionTreeClassifier()
clf_tree.fit(X_train_tree, y_train_tree)
end_time = time.time()
efficiency_tree = end_time - start_time
print("Decision Tree Efficiency (Training):", efficiency_tree)

# Make predictions on the testing set for Decision Tree
y_pred_tree = clf_tree.predict(X_test_tree)

# Calculate the accuracy of the classifier for Decision Tree
accuracy_tree = accuracy_score(y_test_tree, y_pred_tree)
print("Decision Tree Accuracy:", accuracy_tree)
