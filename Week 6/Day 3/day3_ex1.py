# Exercise 1: Apply One-Hot Encoding and Label Encoding to a dataset with categorical variables
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load Titanic dataset
df = pd.read_csv("titanic.csv")

# Display dataset info
print("Dataset Info: ")
print(df.info())

# Preview the first few rows
print("\nDataset Preview:")
print(df.head())

# Apply One-Hot Encoding
df_one_hot = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# Display encoded dataset info
print("Dataset Info: ")
print(df_one_hot.info())

# Display encoded dataset
print("\nOne-Hot Encoded Dataset: ")
print(df_one_hot.head())

# Apply Label Encoding
label_encoder = LabelEncoder()
df['Pclass_encoded'] = label_encoder.fit_transform(df['Pclass'])

# Display encoded dataset info
""" print("Dataset Info: ")
print(df_one_hot.info()) """

# Display encoded dataset
print("\nLabel Encoded Dataset: ")
print(df[['Pclass', 'Pclass_encoded']].head())

# Apply Frequency encoding
df['Ticket_frequency'] = df['Ticket'].map(df['Ticket'].value_counts())

# Display frequency encoded feature
print("\nFrequency Encoded Feature: ")
print(df[['Ticket', 'Ticket_frequency']].head())


# Exercise 2: Experiment with different encoding techniques and observe their impace on model performance
X = df_one_hot.drop(columns=['Survived', 'Age', 'Name', 'Ticket', 'Cabin'])
y = df['Survived']

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("One Hot Data: \n", X)

# Train logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict and evaluate the model
y_pred = model.predict(X_test)
print("Accuracy with One-Hot Encoding: ", accuracy_score(y_test, y_pred))
