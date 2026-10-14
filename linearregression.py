# ==========================================
# HOUSE PRICE PREDICTION
# LINEAR REGRESSION FROM SCRATCH
# GOOGLE COLAB VERSION
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. UPLOAD CSV FILE
# ==========================================

from google.colab import files

uploaded = files.upload()

# Read uploaded CSV file
df = pd.read_csv("housingprice.csv")


# ==========================================
# 2. DISPLAY DATASET
# ==========================================

print("========== HOUSE PRICE DATASET ==========")

print(df.head(10))

print("\nDataset Information:")
df.info()

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Columns:")
print(df.columns)


# ==========================================
# 3. INPUT AND OUTPUT
# ==========================================

# Your CSV columns are:
# sqft       -> House area
# totalprice -> House price

X = df['sqft'].values
Y = df['totalprice'].values


# ==========================================
# 4. LINEAR REGRESSION CLASS
# ==========================================

class LinearRegression:

    # Constructor
    def __init__(self):
        self.slope = 0
        self.intercept = 0

    # Training
    def fit(self, X, Y):

        n = len(X)

        sum_X = np.sum(X)
        sum_Y = np.sum(Y)
        sum_XY = np.sum(X * Y)
        sum_X2 = np.sum(X * X)

        # Calculate slope
        self.slope = (
            (n * sum_XY) - (sum_X * sum_Y)
        ) / (
            (n * sum_X2) - (sum_X * sum_X)
        )

        # Calculate intercept
        self.intercept = (
            sum_Y - (self.slope * sum_X)
        ) / n

    # Prediction
    def predict(self, X):
        return self.slope * X + self.intercept

    # Equation
    def equation(self):
        return (
            f"Price = {self.slope:.2f} × Sqft "
            f"+ {self.intercept:.2f}"
        )

    # Mean Squared Error
    def mse(self, actual, predicted):

        error = actual - predicted

        return np.mean(error ** 2)

    # R2 Score
    def r2_score(self, actual, predicted):

        ss_res = np.sum(
            (actual - predicted) ** 2
        )

        ss_tot = np.sum(
            (actual - np.mean(actual)) ** 2
        )

        return 1 - (ss_res / ss_tot)


# ==========================================
# 5. CREATE AND TRAIN MODEL
# ==========================================

model = LinearRegression()

model.fit(X, Y)


# ==========================================
# 6. MODEL INFORMATION
# ==========================================

print("\n========== MODEL INFORMATION ==========")

print("Slope:", model.slope)

print("Intercept:", model.intercept)

print("\nLinear Regression Equation:")

print(model.equation())


# ==========================================
# 7. PREDICT EXISTING DATA
# ==========================================

Y_pred = model.predict(X)


# ==========================================
# 8. MODEL EVALUATION
# ==========================================

mse = model.mse(Y, Y_pred)

r2 = model.r2_score(Y, Y_pred)

print("\n========== MODEL EVALUATION ==========")

print("Mean Squared Error (MSE):", mse)

print("R² Score:", r2)


# ==========================================
# 9. NEW HOUSE PRICE PREDICTION
# ==========================================

print("\n========== NEW HOUSE PREDICTION ==========")

sqft = float(
    input("Enter house area in sq.ft: ")
)

predicted_price = model.predict(sqft)

print(
    f"\nPredicted price for {sqft:.0f} sq.ft = "
    f"{predicted_price:.2f}"
)


# ==========================================
# 10. GRAPH
# ==========================================

plt.figure(figsize=(10, 6))

# Actual prices
plt.scatter(
    X,
    Y,
    color='green',
    marker='D',
    s=30,
    alpha=0.6,
    label='Actual Prices'
)

# Regression line
X_line = np.linspace(
    X.min(),
    X.max(),
    100
)

Y_line = model.predict(X_line)

plt.plot(
    X_line,
    Y_line,
    color='red',
    linewidth=2,
    label='Regression Line'
)

# New prediction
plt.scatter(
    sqft,
    predicted_price,
    color='blue',
    marker='*',
    s=200,
    label='New Prediction'
)

plt.title(
    'House Price Prediction using Linear Regression'
)

plt.xlabel('Area (sq.ft)')

plt.ylabel('Total Price')

plt.legend()

plt.grid(True)

plt.show()


# ==========================================
# 11. MULTIPLE AREA PREDICTIONS
# ==========================================

print("\n========== MULTIPLE AREA PREDICTIONS ==========")

areas = np.array([
    500,
    750,
    1000,
    1250,
    1500,
    2000,
    2500,
    3000
])

predicted_prices = model.predict(areas)

prediction_df = pd.DataFrame({
    'Area_sqft': areas,
    'Predicted_Price': predicted_prices
})

print(prediction_df)


# ==========================================
# 12. ACTUAL VS PREDICTED
# ==========================================

print("\n========== ACTUAL VS PREDICTED PRICE ==========")

comparison_df = pd.DataFrame({
    'Area_sqft': X[:10],
    'Actual_Price': Y[:10],
    'Predicted_Price': Y_pred[:10]
})

print(comparison_df)
