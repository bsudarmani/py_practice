import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# =========================================================

# LOAD DATASET

# =========================================================

df = pd.read_csv("/content/Elective_Data.csv")

print("\n========== ELECTIVE DATASET ==========")

print(df)

print("\nDataset Shape :", df.shape)

print("\nColumn Names :")

print(df.columns.tolist())

# =========================================================

# REMOVE MISSING VALUES

# =========================================================

df = df.dropna()

# =========================================================

# REMOVE SPACES FROM COLUMN NAMES

# =========================================================

df.columns = df.columns.str.strip()

# =========================================================

# LABEL ENCODING

# =========================================================

gender_encoder = LabelEncoder()

ug_encoder = LabelEncoder()

cross_encoder = LabelEncoder()

elective_encoder = LabelEncoder()

df["GENDER"] = gender_encoder.fit_transform(

    df["GENDER"].astype(str)

)

df["UG"] = ug_encoder.fit_transform(

    df["UG"].astype(str)

)

df["Cross Major"] = cross_encoder.fit_transform(

    df["Cross Major"].astype(str)

)

df["ELECTIVE"] = elective_encoder.fit_transform(

    df["ELECTIVE"].astype(str)

)

print("\n========== ENCODED DATA ==========")

print(df)

# =========================================================

# INPUT AND OUTPUT

# =========================================================

X = df[["GENDER", "UG", "Cross Major"]]

y = df["ELECTIVE"]

# =========================================================

# SPLIT DATASET

# =========================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42,

    stratify=y

)

print("\n========== DATA SPLIT ==========")

print("Training Records :", len(X_train))

print("Testing Records  :", len(X_test))

# =========================================================

# DECISION TREE MODEL

# =========================================================

model = DecisionTreeClassifier(

    criterion="entropy",

    random_state=42

)

# =========================================================

# TRAIN MODEL

# =========================================================

model.fit(

    X_train,

    y_train

)

# =========================================================

# PREDICTION

# =========================================================

y_pred = model.predict(

    X_test

)

# =========================================================

# ACCURACY

# =========================================================

accuracy = accuracy_score(

    y_test,

    y_pred

)

print("\n========== DECISION TREE EVALUATION ==========")

print("Accuracy :", accuracy * 100, "%")

# =========================================================

# CONFUSION MATRIX

# =========================================================

print("\n========== CONFUSION MATRIX ==========")

print(confusion_matrix(

    y_test,

    y_pred

))

# =========================================================

# CLASSIFICATION REPORT

# =========================================================

print("\n========== CLASSIFICATION REPORT ==========")

print(classification_report(

    y_test,

    y_pred,

    zero_division=0

))

# =========================================================

# RUNTIME INPUT

# =========================================================

print("\n========== ELECTIVE PREDICTION ==========")

gender = input(

    "Enter Gender (F/M) : "

).strip().upper()

ug = input(

    "Enter UG (Phy/BCA/Com) : "

).strip()

cross_major = input(

    "Enter Cross Major (Y/N) : "

).strip().upper()

# =========================================================

# VALIDATE INPUT

# =========================================================

if gender not in gender_encoder.classes_:

    print("\nInvalid Gender!")

    print("Available values :", list(gender_encoder.classes_))

    exit()

if ug not in ug_encoder.classes_:

    print("\nInvalid UG!")

    print("Available values :", list(ug_encoder.classes_))

    exit()

if cross_major not in cross_encoder.classes_:

    print("\nInvalid Cross Major!")

    print("Available values :", list(cross_encoder.classes_))

    exit()

# =========================================================

# ENCODE RUNTIME INPUT

# =========================================================

gender_value = gender_encoder.transform(

    [gender]

)[0]

ug_value = ug_encoder.transform(

    [ug]

)[0]

cross_value = cross_encoder.transform(

    [cross_major]

)[0]

# =========================================================

# CREATE NEW STUDENT

# =========================================================

new_student = pd.DataFrame(

    [[gender_value, ug_value, cross_value]],

    columns=["GENDER", "UG", "Cross Major"]

)

# =========================================================

# PREDICT ELECTIVE

# =========================================================

prediction = model.predict(

    new_student

)

# =========================================================

# CONVERT PREDICTION TO ORIGINAL ELECTIVE

# =========================================================

elective_name = elective_encoder.inverse_transform(

    prediction

)[0]

# =========================================================

# RESULT

# =========================================================

print("\n========== PREDICTION RESULT ==========")

print("Gender       :", gender)

print("UG           :", ug)

print("Cross Major  :", cross_major)

print("\nPredicted Elective :", elective_name)


