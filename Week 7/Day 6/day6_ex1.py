# Exercise 1: Apply SMOTE o handle class imbalance, train a classifier, and evaluate its performance using metrics like ROC-AUC and F1-score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from imblearn.over_sampling import SMOTE

# Load dataset
url = "https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"
df = pd.read_csv(url)

# Explore dataset
print("Dataset Info:\n")
print(df.info())
print("\nClass Distribution:\n")
print(df["Class"].value_counts())

# Split dataset
X = df.drop(columns=['Class'])
y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest
rf_model = RandomForestClassifier(random_state=42, class_weight="balanced")
rf_model.fit(X_train, y_train)

# Predict and evaluate
y_pred = rf_model.predict(X_test)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

roc_auc = roc_auc_score(y_test, rf_model.predict_proba(X_test)[:,1])
print(f"ROC-AUC: {roc_auc:.2f}")

# Apply SMOTE
smote = SMOTE(random_state=42)
X_resample, y_resample = smote.fit_resample(X_train, y_train)

# Display new class distribution
print("\n Class Distribution After SMOTE: \n")
print(pd.Series(y_resample).value_counts())

# Train Random Forest on Resampled data
rf_model_smote = RandomForestClassifier(random_state=42, class_weight="balanced")
rf_model_smote.fit(X_resample, y_resample)

# Predict and evaluate
y_pred_smote = rf_model_smote.predict(X_test)
print("\nClassification Report (SMOTE):\n")
print(classification_report(y_test, y_pred_smote))

roc_auc_smote = roc_auc_score(y_test, rf_model_smote.predict_proba(X_test)[:,1])
print(f"ROC-AUC (SMOTE): {roc_auc_smote:.2f}")
