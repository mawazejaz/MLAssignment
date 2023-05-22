import csv
import math
from collections import Counter

def entropy(data):
    labels = [record[-1] for record in data]
    label_counts = Counter(labels)
    total_records = len(data)
    entropy_value = 0.0
    for count in label_counts.values():
        probability = count / total_records
        entropy_value -= probability * math.log2(probability)
    return entropy_value

def split_data(data, attribute_index):
    attribute_values = set(record[attribute_index] for record in data)
    split_data = {}
    for value in attribute_values:
        split_data[value] = [record for record in data if record[attribute_index] == value]
    return split_data

def select_attribute(data, attributes):
    data_entropy = entropy(data)
    max_info_gain = -1
    selected_attribute = None
    for attribute_index in attributes:
        attribute_values = set(record[attribute_index] for record in data)
        attribute_entropy = 0.0
        for value in attribute_values:
            subset = [record for record in data if record[attribute_index] == value]
            subset_entropy = entropy(subset)
            subset_probability = len(subset) / len(data)
            attribute_entropy += subset_probability * subset_entropy
        info_gain = data_entropy - attribute_entropy
        if info_gain > max_info_gain:
            max_info_gain = info_gain
            selected_attribute = attribute_index
    return selected_attribute

def majority_class(data):
    labels = [record[-1] for record in data]
    label_counts = Counter(labels)
    majority_label = label_counts.most_common(1)[0][0]
    return majority_label

def build_decision_tree(data, attributes):
    labels = [record[-1] for record in data]
    if len(set(labels)) == 1:
        return labels[0]
    if len(attributes) == 0:
        return majority_class(data)
    selected_attribute = select_attribute(data, attributes)
    tree = {selected_attribute: {}}
    remaining_attributes = attributes - {selected_attribute}
    attribute_values = set(record[selected_attribute] for record in data)
    for value in attribute_values:
        subset = [record for record in data if record[selected_attribute] == value]
        subtree = build_decision_tree(subset, remaining_attributes)
        tree[selected_attribute][value] = subtree
    return tree

def predict(record, tree):
    if isinstance(tree, str):
        return tree
    attribute = next(iter(tree))
    attribute_value = record[attribute]
    subtree = tree[attribute].get(attribute_value)
    if subtree is None:
        return None
    return predict(record, subtree)


# Download and preprocess data from the CSV file
data = []
with open('weather.csv', 'r') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)
    for row in csv_reader:
        data.append(row)

# Convert numerical values to float
for i in range(len(data)):
    for j in range(len(data[i]) - 1):
        data[i][j] = float(data[i][j])

# Convert the last column to the target labels
for i in range(len(data)):
    data[i][-1] = str(data[i][-1])

# Define the attributes (excluding the target column)
attributes = set(range(len(headers) - 1))

# Build the decision tree
tree = build_decision_tree(data, attributes)

# Example prediction
test_record = {'air_pressure_9am': 918.0, 'air_temp_9am': 72.0, 'avg_wind_direction_9am': 135.0,
               'avg_wind_speed_9am': 2.0, 'max_wind_direction_9am': 135.0, 'max_wind_speed_9am': 2.0,
               'rain_accumulation_9am': 0.0, 'rain_duration_9am': 0.0}
prediction = predict(test_record, tree)
print("Prediction:", prediction)
