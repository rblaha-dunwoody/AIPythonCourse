# Project: Build, tune, and optimize a machine learning model using a structured process and evaluate its performance comprehensively
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, RandomizedSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Load data set
df = pd.read_csv("Telco-Customer-Churn.xls")

# Display dataset info
print("Dataset Info:\n")
print(df.info())
print("\nClass Distribution:\n")
print(df['Churn'].value_counts())
print("\nSample Data:\n", df.head())

# Notice how this is an imbalanced dataset, as there are substantially more No's than Yes's in the target data
# No     5174
# Yes    1869

# Handle missing values
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.fillna({'TotalCharges': df['TotalCharges'].median()}, inplace=True)

# Encode categorical variables
label_encoder = LabelEncoder()
for column in df.select_dtypes(include=['object']).columns:
    if column != 'Churn':
        df[column] = label_encoder.fit_transform(df[column])

# Encode target variable
df['Churn'] = label_encoder.fit_transform(df['Churn'])

# Scale the numerical features
scaler = StandardScaler()
numerical_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
df[numerical_features] = scaler.fit_transform(df[numerical_features])

# Features and Target
X = df.drop(columns=['Churn'])
y = df['Churn']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train initial model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Evaluate initial model
y_pred = rf_model.predict(X_test)
accuracy_initial = accuracy_score(y_test, y_pred)

# View the output of the initial model (no tuning has been done up to this point)
print(f"Initial Model Accurady: {accuracy_initial:.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))
        
# Define parameter grid
param_dist = {
    'n_estimators': np.arange(50, 200, 10),
    'max_depth': [None, 5, 10, 15],
    'min_samples_split': [2, 5, 10, 20],
    'min_samples_leaf': [1, 2, 4]
}

# Initialize RandomizedSearchCV
random_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=20,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    random_state=42
)

# Perform Randomized Search
print("Performing RandomizedSearchCV...")
random_search.fit(X_train, y_train)
print("RandomizedSearchCV complete!")

# Get best parameters
best_params = random_search.best_params_
print(f"Best Parameters (RandomizedSearchCV): {best_params}")

# Train best model 
best_model = random_search.best_estimator_

# Predict and Evaluate
y_pred_tuned = best_model.predict(X_test)
accuracy_tuned = accuracy_score(y_test, y_pred_tuned)

print(f"Tuned Model Accuracy: {accuracy_tuned:.4f}")
print("\nClassification Report (Tuned Model):\n", classification_report(y_test, y_pred_tuned))

# Evaluate using cross-validation
print("Performing Cross-Validation...")
cv_scores = cross_val_score(best_model, X, y, cv=5, scoring='accuracy')
print("Cross-Validation complete!")

print(f"Cross-Validation Accuracy Scores: {cv_scores}")
print(f"Mean Cross-Validatoin Accuracy: {cv_scores.mean():.4f}")
