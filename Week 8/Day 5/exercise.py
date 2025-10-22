# Evaluate a classification model using K-Fold and Stratified K-Fold Cross-Validation
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, KFold, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("../../../Resources/AIPythonCourse/creditcard.csv")

# Display dataset info
print("Dataset Info:\n")
print(df.info())
print("\nClass Distribution:\n")
print(df['Class'].value_counts())

# Define Features and target
X = df.drop(columns=['Class'])
y = df['Class']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize K-Fold
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Train and evaluate model
print("Performing K-Fold Cross-Validation...")
rf_model = RandomForestClassifier(random_state=42)
scores_kfold = cross_val_score(rf_model, X_train, y_train, cv=kf, scoring='accuracy')
print("K-Fold Cross-Validation complete!")

print(f"K-Fold Cross Validation Scores: {scores_kfold}")
print(f"Mean Accuracy (K-Fold): {scores_kfold.mean():.2f}")

# Initialize Stratified K-Fold
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Train and evaluate model
print("Performing Stratified K-Fold Cross-Validation...")
scores_stratified = cross_val_score(rf_model, X_train, y_train, cv=skf, scoring='accuracy')
print("Stratified K-Fold Cross-Validation complete!")

print(f"Stratified K-Fold Cross Validation Scores: {scores_stratified}")
print(f"Mean Accuracy (StratifiedK-Fold): {scores_stratified.mean():.2f}")
