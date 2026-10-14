```python
# Import libraries
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# 1. Load Iris dataset
irisData = load_iris()

print("IRIS DATASET")
print(irisData)

# 2. Create features and target
X = irisData.data
y = irisData.target

print("\nFeatures:")
print(X)

print("\nTarget:")
print(y)

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data:", len(X_train))
print("Testing data:", len(X_test))

# 4. Create KNN model
knn = KNeighborsClassifier(n_neighbors=7)

# 5. Train model
knn.fit(X_train, y_train)

# 6. Prediction
y_predict = knn.predict(X_test)

print("\nPredicted Labels:")
print(y_predict)

# 7. Confusion Matrix
result = confusion_matrix(y_test, y_predict)

print("\nConfusion Matrix:")
print(result)

# 8. Classification Report
result1 = classification_report(
    y_test,
    y_predict
)

print("\nClassification Report:")
print(result1)

# 9. Accuracy
result2 = accuracy_score(
    y_test,
    y_predict
)

print("Accuracy:", result2)
```
