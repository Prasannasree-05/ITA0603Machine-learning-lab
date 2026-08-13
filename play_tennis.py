import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Create the dataset
data = {
    'Sky': [
        'Sunny', 'Sunny', 'Rainy', 'Sunny',
        'Rainy', 'Sunny', 'Cloudy', 'Sunny'
    ],

    'Temperature': [
        'Warm', 'Warm', 'Cold', 'Warm',
        'Warm', 'Warm', 'Warm', 'Cold'
    ],

    'Humidity': [
        'Normal', 'High', 'High', 'High',
        'Normal', 'Normal', 'Normal', 'High'
    ],

    'Wind': [
        'Strong', 'Strong', 'Strong', 'Strong',
        'Weak', 'Weak', 'Strong', 'Weak'
    ],

    'Water': [
        'Warm', 'Warm', 'Warm', 'Cool',
        'Warm', 'Warm', 'Warm', 'Cool'
    ],

    'Forecast': [
        'Same', 'Same', 'Change', 'Same',
        'Same', 'Same', 'Same', 'Change'
    ],

    'PlayTennis': [
        'Yes', 'Yes', 'No', 'Yes',
        'No', 'Yes', 'Yes', 'No'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Convert categorical values into numbers
encoder = LabelEncoder()

for column in df.columns:
    df[column] = encoder.fit_transform(df[column])

# Input attributes
X = df[['Sky', 'Temperature', 'Humidity',
        'Wind', 'Water', 'Forecast']]

# Target attribute
y = df['PlayTennis']

# Create Decision Tree using ID3
model = DecisionTreeClassifier(
    criterion='entropy',
    random_state=42
)

# Train the model
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Display actual and predicted values
print("\nActual values:")
print(y.values)

print("\nPredicted values:")
print(y_pred)

# Calculate accuracy
accuracy = accuracy_score(y, y_pred)

print("\nAccuracy:", accuracy)
