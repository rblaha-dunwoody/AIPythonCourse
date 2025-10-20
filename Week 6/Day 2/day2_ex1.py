# Exercise 1: Apply Min-Max Scaling and Standardization to a Dataset using scikit-learn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd

# Load iris dataset
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Display dataset information
print("Dataset Info: ")
print(X.describe())
print("\nTarget Classes: ", data.target_names)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the k-NN classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict and evaluate
y_pred = knn.predict(X_test)
print("Accuracy Without Scaling: ", accuracy_score(y_test, y_pred))


# Exercise 2: Observe the Effects of Scaling on Model Performance by Training a k-NN Classifier Before and After Scaling
# Apply Min-Max Scaling
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Split scaled data
X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train k-NN classifier on scaled data
knn_scaled = KNeighborsClassifier(n_neighbors=5)
knn_scaled.fit(X_train_scaled, y_train_scaled)

# Predict and evaluate
y_pred_scaled = knn_scaled.predict(X_test_scaled)
print("Accuracy With Min-Max Scaling: ", accuracy_score(y_test_scaled, y_pred_scaled))


# Exercise 3: Apply Standardization
# Apply Standardization
scaler_standard = StandardScaler()
X_standard = scaler_standard.fit_transform(X)

# Split scaled data
X_train_standard, X_test_standard, y_train_standard, y_test_standard = train_test_split(X_standard, y, test_size=0.2, random_state=42)

# Train k-NN classifier on scaled data
knn_standard = KNeighborsClassifier(n_neighbors=5)
knn_standard.fit(X_train_standard, y_train_standard)

# Predict and evaluate
y_pred_standard = knn_standard.predict(X_test_standard)
print("Accuracy With Standardization: ", accuracy_score(y_test_standard, y_pred_standard))


