```python
import pandas as pd

# Load Dataset
df = pd.read_csv("data.csv")

while True:

    print("\n========== DATASET ANALYSIS MENU ==========")
    print("1. Display Dataset")
    print("2. Display First 5 Rows")
    print("3. Display Last 5 Rows")
    print("4. Display Dataset Shape")
    print("5. Display Column Names")
    print("6. Display Data Types")
    print("7. Display Dataset Information")
    print("8. Display Statistical Summary")
    print("9. Display Mean")
    print("10. Display Median")
    print("11. Display Mode")
    print("12. Display Minimum and Maximum")
    print("13. Display Standard Deviation")
    print("14. Display Variance")
    print("15. Display Missing Values")
    print("16. Exit")
    print("===========================================")

    ch = int(input("Enter your choice: "))

    # 1. Display Dataset
    if ch == 1:
        print("\nDataset:")
        print(df)

    # 2. First 5 Rows
    elif ch == 2:
        print("\nFirst 5 Rows:")
        print(df.head())

    # 3. Last 5 Rows
    elif ch == 3:
        print("\nLast 5 Rows:")
        print(df.tail())

    # 4. Dataset Shape
    elif ch == 4:
        print("\nDataset Shape:")
        print(df.shape)

        print("Number of Rows:", df.shape[0])
        print("Number of Columns:", df.shape[1])

    # 5. Column Names
    elif ch == 5:
        print("\nColumn Names:")
        print(df.columns)

    # 6. Data Types
    elif ch == 6:
        print("\nData Types:")
        print(df.dtypes)

    # 7. Dataset Information
    elif ch == 7:
        print("\nDataset Information:")
        df.info()

    # 8. Statistical Summary
    elif ch == 8:
        print("\nStatistical Summary:")
        print(df.describe())

    # 9. Mean
    elif ch == 9:
        print("\nMean:")
        print(df.select_dtypes(include="number").mean())

    # 10. Median
    elif ch == 10:
        print("\nMedian:")
        print(df.select_dtypes(include="number").median())

    # 11. Mode
    elif ch == 11:
        print("\nMode:")
        print(df.select_dtypes(include="number").mode())

    # 12. Minimum and Maximum
    elif ch == 12:
        numeric = df.select_dtypes(include="number")

        print("\nMinimum Values:")
        print(numeric.min())

        print("\nMaximum Values:")
        print(numeric.max())

    # 13. Standard Deviation
    elif ch == 13:
        print("\nStandard Deviation:")
        print(df.select_dtypes(include="number").std())

    # 14. Variance
    elif ch == 14:
        print("\nVariance:")
        print(df.select_dtypes(include="number").var())

    # 15. Missing Values
    elif ch == 15:
        print("\nMissing Values:")
        print(df.isnull().sum())

    # 16. Exit
    elif ch == 16:
        print("\nProgram exited successfully!")
        break

    else:
        print("\nInvalid choice! Please enter 1 to 16.")
```

### Example `data.csv`

You can create a `data.csv` file in the same folder as your Python program:

```text
Name,Age,Mark,Department
Arun,20,85,CSE
Bala,21,90,IT
Kumar,20,75,CSE
Priya,22,95,IT
Ravi,21,80,CSE
```

### Main concepts covered

| Category | Options |
|---|---|
| **Loading** | `pd.read_csv()` |
| **Dataset structure** | `shape`, `columns`, `dtypes`, `info()` |
| **Data viewing** | `head()`, `tail()` |
| **Statistical analysis** | `describe()`, `mean()`, `median()`, `mode()` |
| **Statistical measures** | `min()`, `max()`, `std()`, `var()` |
| **Data quality** | `isnull()` |

### Important functions for your practical

Remember these:

```python
pd.read_csv()       # Load dataset
df.head()           # First rows
df.tail()           # Last rows
df.shape             # Rows and columns
df.columns           # Column names
df.dtypes            # Data types
df.info()            # Structure/information
df.describe()        # Statistical summary
df.mean()            # Mean
df.median()          # Median
df.mode()            # Mode
df.min()             # Minimum
df.max()             # Maximum
df.std()             # Standard deviation
df.var()             # Variance
df.isnull()          # Missing values
```

This single program covers the typical **"Load a dataset, understand its structure, and perform statistical analysis"** practical question.
