
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Rest of the code...

# Prepare the data
data = pd.read_csv('GroceryStoreDataSet.csv', header=None)
transactions = []
for i in range(len(data)):
    transactions.append(data.values[i, 0].split(','))

# Create the Apriori class
model = Apriori(transactions, min_support=0.2, min_confidence=0.5)
L = model.generate_L()

# Prepare the dataset for classification
X = []
y = []
for transaction in transactions:
    row = [1 if item in transaction else 0 for itemset in L for item in itemset]
    X.append(row)
    y.append(1)  # We assume all transactions are positive examples

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = clf.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
