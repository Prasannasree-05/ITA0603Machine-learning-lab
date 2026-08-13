import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Read the Excel dataset
data = pd.read_excel("disease_data.xlsx")

print("Dataset:")
print(data)

# Convert categorical values into numbers
encoder = LabelEncoder()

for column in data.columns:
    data[column] = encoder.fit_transform(data[column])

# Input features
X = data[['Fever', 'Cough', 'Headache', 'BodyPain', 'Fatigue']]

# Target attribute
y = data['Disease']

# Create Decision Tree
model = DecisionTreeClassifier(criterion='entropy', random_state=42)

# Train the model
model.fit(X, y)

# Predict the same dataset
y_pred = model.predict(X)

print("\nActual Disease:")
print(y.values)

print("\nPredicted Disease:")
print(y_pred)

# Calculate accuracy
accuracy = accuracy_score(y, y_pred)

print("\nAccuracy:", accuracy)
