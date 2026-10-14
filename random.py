# ---- 1. Import required libraries ----
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix,
                              classification_report, ConfusionMatrixDisplay)

# ---- 2. Load the dataset ----
df = pd.read_csv("customer_churn_dataset.csv")
print("Dataset shape:", df.shape)
print(df['Churn'].value_counts())


# ---- 3. Basic data cleaning ----
# TotalCharges is stored as text and has a few blank entries -> convert to numeric
#If pandas encounters a value that cannot be converted into a number, replace it with NaN, errors='coerce'
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())

# customerID is just an identifier, not predictive -> drop it
df = df.drop(columns=['customerID'])

# ---- 4. Encode categorical (text) columns into numbers ----
# Get all object columns present in the DataFrame at this point
all_object_cols = df.select_dtypes(include=['object']).columns.tolist()

# Identify columns to be encoded by the main loop (excluding 'Churn')
# This also handles cases where 'Churn' might have already been processed
cat_cols = [col for col in all_object_cols if col != 'Churn']

label_encoders = {}
for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Handle 'Churn' separately, only if it is still an object type
# This prevents errors if 'Churn' is already numeric from a previous run
if 'Churn' in all_object_cols:
    target_le = LabelEncoder()
    df['Churn'] = target_le.fit_transform(df['Churn'])  # No=0, Yes=1



# ---- 5. Separate features (X) and target (y) ----
X = df.drop(columns=['Churn'])
y = df['Churn']
# ---- 6. Split into training and testing sets ----
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ---- 7. Create and train the Random Forest model ----
rf_model = RandomForestClassifier(
    n_estimators=200,     # number of trees in the forest
    max_depth=8,           # limit tree depth to reduce overfitting
    random_state=42,
    n_jobs=-1               # use all CPU cores
)
rf_model.fit(X_train, y_train)

# ---- 8. Make predictions ----
y_pred = rf_model.predict(X_test)

# ---- 9. Evaluate the model ----
acc = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {acc*100:.2f}%")
print("\nClassification Report:\n", classification_report(
    y_test, y_pred, target_names=['No Churn', 'Churn']))

# ---- 10. Confusion Matrix ----
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                               display_labels=['No Churn', 'Churn'])
disp.plot(cmap='Greens')
plt.title("Random Forest - Confusion Matrix (Customer Churn)")
plt.tight_layout()
plt.savefig("rf_confusion_matrix.png", dpi=150)

# ---- 11. Feature importance -> which factors drive the decision ----
importances = pd.Series(rf_model.feature_importances_, index=X.columns)
importances = importances.sort_values(ascending=False).head(10)

plt.figure(figsize=(8, 5))
importances.plot(kind='barh')
plt.gca().invert_yaxis()
plt.title("Top 10 Features Driving Customer Churn")
plt.xlabel("Importance Score")
plt.tight_layout()
plt.savefig("rf_feature_importance.png", dpi=150)

print("\nTop 5 factors influencing churn decisions:")
print(importances.head(5))
