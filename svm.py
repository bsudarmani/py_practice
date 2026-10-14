```python
# ============================================================
# SVM CLASSIFICATION - BREAST CANCER DATASET
# ============================================================

# 1. Import required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)


# ============================================================
# 2. Load the dataset
# ============================================================

df = pd.read_csv("breast_cancer_dataset.csv")

print("\n================ DATASET ================")
print(df)

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDiagnosis Label Count:")
print(df["diagnosis_label"].value_counts())


# ============================================================
# 3. Separate Features (X) and Target (y)
# ============================================================

# Remove target-related columns from X
X = df.drop(columns=["diagnosis", "diagnosis_label"])

# Target column
y = df["diagnosis"]

print("\n================ FEATURES (X) ================")
print(X)

print("\n================ TARGET (y) ================")
print(y)


# ============================================================
# 4. Split Dataset into Training and Testing
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\n================ DATA SPLIT ================")

print("Training samples:", X_train.shape[0])
print("Testing samples :", X_test.shape[0])


# ============================================================
# 5. Feature Scaling
# ============================================================

scaler = StandardScaler()

# Fit and transform training data
X_train_scaled = scaler.fit_transform(X_train)

# Transform testing data
X_test_scaled = scaler.transform(X_test)

print("\nFeature scaling completed.")


# ============================================================
# 6. Create SVM Model - RBF Kernel
# ============================================================

svm_model = SVC(
    kernel="rbf",
    C=1.0,
    gamma="scale",
    random_state=42
)


# ============================================================
# 7. Train the RBF SVM Model
# ============================================================

svm_model.fit(
    X_train_scaled,
    y_train
)

print("\nRBF SVM model training completed.")


# ============================================================
# 8. Predict Test Data
# ============================================================

y_pred = svm_model.predict(X_test_scaled)

print("\n================ PREDICTED VALUES ================")
print(y_pred)


# ============================================================
# 9. Calculate Accuracy
# ============================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\n================ RBF SVM ACCURACY ================")

print(
    f"Accuracy: {accuracy * 100:.2f}%"
)


# ============================================================
# 10. Classification Report
# ============================================================

print("\n================ CLASSIFICATION REPORT ================")

report = classification_report(
    y_test,
    y_pred,
    target_names=[
        "malignant",
        "benign"
    ]
)

print(report)


# ============================================================
# 11. Confusion Matrix
# ============================================================

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\n================ CONFUSION MATRIX ================")

print(cm)


# ============================================================
# 12. Display Confusion Matrix
# ============================================================

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=[
        "malignant",
        "benign"
    ]
)

disp.plot(cmap="Blues")

plt.title(
    "SVM - Confusion Matrix (Breast Cancer Diagnosis)"
)

plt.tight_layout()

# Save confusion matrix image
plt.savefig(
    "svm_confusion_matrix.png",
    dpi=150
)

plt.show()


# ============================================================
# 13. Linear Kernel SVM
# ============================================================

svm_linear = SVC(
    kernel="linear",
    C=1.0,
    random_state=42
)


# ============================================================
# 14. Train Linear SVM
# ============================================================

svm_linear.fit(
    X_train_scaled,
    y_train
)


# ============================================================
# 15. Linear SVM Prediction
# ============================================================

y_pred_linear = svm_linear.predict(
    X_test_scaled
)


# ============================================================
# 16. Linear SVM Accuracy
# ============================================================

accuracy_linear = accuracy_score(
    y_test,
    y_pred_linear
)


# ============================================================
# 17. Compare RBF and Linear Kernel
# ============================================================

print("\n================ KERNEL COMPARISON ================")

print(
    f"Linear Kernel Accuracy : "
    f"{accuracy_linear * 100:.2f}%"
)

print(
    f"RBF Kernel Accuracy    : "
    f"{accuracy * 100:.2f}%"
)


# ============================================================
# 18. Final Result
# ============================================================

print("\n================ FINAL RESULT ================")

if accuracy > accuracy_linear:

    print("RBF Kernel gives better accuracy.")

elif accuracy_linear > accuracy:

    print("Linear Kernel gives better accuracy.")

else:

    print("Both kernels give the same accuracy.")


# ============================================================
# END OF PROGRAM
# ============================================================
```
