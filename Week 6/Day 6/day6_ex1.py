# Exercise 1: Classifcation Model Evaluation
# Objective: Train a classification model, calculate the confusion matrix, and interpret precision, recall and F1 Score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Load the dataset
data = load_iris()
X = data.data
y = (data.target == 0).astype(int)

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_predict = model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_predict)
display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Not Class 0", "Class 0"])
display.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.show()

# Classification metrics
print("\n Classification Report: ")
print(classification_report(y_test, y_predict))



