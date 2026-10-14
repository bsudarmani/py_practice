# =========================================================

# 1. IMPORT LIBRARIES

# =========================================================

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import (

    accuracy_score,

    confusion_matrix,

    ConfusionMatrixDisplay,

    f1_score,

    classification_report

)

# =========================================================

# 2. LOAD DATASET

# =========================================================

df = pd.read_csv(
'content/loan.csv'
)

print("First 5 rows:")

print(df.head())

print("\nDataset Information:")

df.info()

# =========================================================

# 3. VISUALIZE PURPOSE VS LOAN PAYMENT

# =========================================================

sns.countplot(

    data=df,

    x='purpose',

    hue='not.fully.paid'

)

plt.xticks(rotation=45, ha='right')

plt.title('Loan Purpose vs Not Fully Paid')

plt.xlabel('Loan Purpose')

plt.ylabel('Count')

plt.show()

# =========================================================

# 4. CONVERT CATEGORICAL DATA INTO NUMERIC DATA

# =========================================================

pre_df = pd.get_dummies(

    df,

    columns=['purpose'],

    drop_first=True

)

print("\nPreprocessed Dataset:")

print(pre_df.head())

# =========================================================

# 5. DEFINE INPUT (X) AND OUTPUT (Y)

# =========================================================

X = pre_df.drop('not.fully.paid', axis=1)

y = pre_df['not.fully.paid']

print("\nInput Features (X):")

print(X)

print("\nTarget (y):")

print(y)

# =========================================================

# 6. SPLIT DATASET INTO TRAINING AND TESTING DATA

# =========================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.33,

    random_state=125

)

print("\nTraining Data:", X_train.shape)

print("Testing Data:", X_test.shape)

# =========================================================

# 7. CREATE NAIVE BAYES MODEL

# =========================================================

model = GaussianNB()

# =========================================================

# 8. TRAIN THE MODEL

# =========================================================

model.fit(X_train, y_train)

# =========================================================

# 9. MAKE PREDICTIONS

# =========================================================

y_pred = model.predict(X_test)

# =========================================================

# 10. CALCULATE ACCURACY

# =========================================================

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

# =========================================================

# 11. CALCULATE F1 SCORE

# =========================================================

f1 = f1_score(

    y_test,

    y_pred,

    average='weighted'

)

print("F1 Score:", f1)

# =========================================================

# 12. CONFUSION MATRIX

# =========================================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")

print(cm)

disp = ConfusionMatrixDisplay(

    confusion_matrix=cm

)

disp.plot()

plt.title("Confusion Matrix - Naive Bayes")

plt.show()

# =========================================================

# 13. CLASSIFICATION REPORT

# =========================================================

print("\nClassification Report:")

print(classification_report(y_test, y_pred))
