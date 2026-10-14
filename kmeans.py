```python
# ============================================================
# K-MEANS CLUSTERING - MALL CUSTOMER SEGMENTATION
# ============================================================

# ------------------------------------------------------------
# 1. Mount Google Drive
# ------------------------------------------------------------

from google.colab import drive

drive.mount('/content/drive')


# ------------------------------------------------------------
# 2. Import Required Libraries
# ------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

import warnings
warnings.filterwarnings('ignore')


# ------------------------------------------------------------
# 3. Load the Dataset
# ------------------------------------------------------------

customer_data = pd.read_csv(
    "/content/drive/MyDrive/Colab Notebooks/Mall_Customers.csv"
)


# ------------------------------------------------------------
# 4. Display Dataset Shape
# ------------------------------------------------------------

print("Dataset Shape:")
print(customer_data.shape)


# ------------------------------------------------------------
# 5. Display Dataset Information
# ------------------------------------------------------------

print("\nDataset Information:")
customer_data.info()


# ------------------------------------------------------------
# 6. Check Missing Values
# ------------------------------------------------------------

print("\nMissing Values:")
print(customer_data.isnull().sum())


# ------------------------------------------------------------
# 7. Display First 5 Rows
# ------------------------------------------------------------

print("\nFirst 5 Rows:")
print(customer_data.head())


# ------------------------------------------------------------
# 8. Select Features
# ------------------------------------------------------------
# Column index 3 = Annual Income (k$)
# Column index 4 = Spending Score (1-100)

X = customer_data.iloc[:, [3, 4]].values

print("\nSelected Features:")
print(X[:25])


# ------------------------------------------------------------
# 9. Find Optimal Number of Clusters using Elbow Method
# ------------------------------------------------------------

from sklearn.cluster import KMeans

wcss = []

for i in range(1, 11):

    kmeans = KMeans(
        n_clusters=i,
        init='k-means++',
        random_state=42,
        n_init=10
    )

    kmeans.fit(X)

    wcss.append(kmeans.inertia_)


# ------------------------------------------------------------
# 10. Plot Elbow Graph
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    range(1, 11),
    wcss,
    marker='o'
)

plt.title('The Elbow Point Graph')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')

plt.grid(True)

plt.show()


# ------------------------------------------------------------
# 11. Create K-Means Model with 5 Clusters
# ------------------------------------------------------------
# From the elbow graph, K = 5 is normally selected
# for the Mall Customers dataset.

kmeans = KMeans(
    n_clusters=5,
    init='k-means++',
    random_state=42,
    n_init=10
)


# ------------------------------------------------------------
# 12. Train the K-Means Model
# ------------------------------------------------------------

y = kmeans.fit_predict(X)


# ------------------------------------------------------------
# 13. Display Cluster Labels
# ------------------------------------------------------------

print("\nCluster Labels:")
print(y)


# ------------------------------------------------------------
# 14. Display Cluster Centers
# ------------------------------------------------------------

print("\nCluster Centroids:")

print(kmeans.cluster_centers_)


# ------------------------------------------------------------
# 15. Add Cluster Number to Dataset
# ------------------------------------------------------------

customer_data['Cluster'] = y + 1

print("\nDataset with Cluster:")
print(customer_data.head(10))


# ------------------------------------------------------------
# 16. Plot All 5 Clusters
# ------------------------------------------------------------

plt.figure(figsize=(8, 8))

# Cluster 1
plt.scatter(
    X[y == 0, 0],
    X[y == 0, 1],
    s=50,
    label='Cluster 1'
)

# Cluster 2
plt.scatter(
    X[y == 1, 0],
    X[y == 1, 1],
    s=50,
    label='Cluster 2'
)

# Cluster 3
plt.scatter(
    X[y == 2, 0],
    X[y == 2, 1],
    s=50,
    label='Cluster 3'
)

# Cluster 4
plt.scatter(
    X[y == 3, 0],
    X[y == 3, 1],
    s=50,
    label='Cluster 4'
)

# Cluster 5
plt.scatter(
    X[y == 4, 0],
    X[y == 4, 1],
    s=50,
    label='Cluster 5'
)


# ------------------------------------------------------------
# 17. Plot Centroids
# ------------------------------------------------------------

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=200,
    marker='X',
    label='Centroids'
)


# ------------------------------------------------------------
# 18. Add Graph Details
# ------------------------------------------------------------

plt.title('Customer Groups')

plt.xlabel('Annual Income (k$)')

plt.ylabel('Spending Score (1-100)')

plt.legend()

plt.grid(True)

plt.show()


# ------------------------------------------------------------
# 19. Display Number of Customers in Each Cluster
# ------------------------------------------------------------

print("\nNumber of Customers in Each Cluster:")

print(
    customer_data['Cluster'].value_counts().sort_index()
)


# ------------------------------------------------------------
# 20. Display Average Income and Spending Score
# ------------------------------------------------------------

cluster_summary = customer_data.groupby('Cluster')[
    ['Annual Income (k$)', 'Spending Score (1-100)']
].mean()

print("\nCluster Summary:")
print(cluster_summary)


# ------------------------------------------------------------
# 21. Visualize Cluster Summary
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.barplot(
    data=cluster_summary.reset_index(),
    x='Cluster',
    y='Spending Score (1-100)'
)

plt.title('Average Spending Score by Cluster')

plt.xlabel('Cluster')

plt.ylabel('Average Spending Score')

plt.show()
```
