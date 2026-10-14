import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt

# Load Iris dataset
iris = load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Create Extra Trees Classifier
model = ExtraTreesClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X, y)

# Get feature importance
importance = model.feature_importances_

# Display feature importance
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importance
})

feature_importance = feature_importance.sort_values(
    by='Importance',
    ascending=False
)

print("Feature Importance:")
print(feature_importance)

# Plot feature importance
plt.figure(figsize=(8, 5))
plt.bar(
    feature_importance['Feature'],
    feature_importance['Importance']
)

plt.xticks(rotation=45)
plt.xlabel("Features")
plt.ylabel("Importance")
plt.title("Feature Selection using Extra Trees Classifier")
plt.tight_layout()
plt.show()
