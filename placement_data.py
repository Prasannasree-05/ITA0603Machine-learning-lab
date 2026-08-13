import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Read Excel file
data = pd.read_excel("placement_data.xlsx")

print("Dataset:")
print(data)

# Convert categorical data into numbers
encoder = LabelEncoder()

for column in data.columns:
    data[column] = encoder.fit_transform(data[column])

# Input features
X = data[['CGPA', 'Communication', 'Internship',
          'Programming', 'Aptitude']]

# Target variable
y = data['Placed']

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Decision Tree model
model = DecisionTreeClassifier(
    criterion='entropy',
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Display results
print("\nActual values:")
print(y_test.values)

print("\nPredicted values:")
print(y_pred)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)
