import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


iris_df = pd.read_csv(r'C:/Users/dell/Downloads/iris-flower-dataset.csv')


X = iris_df.iloc[:, :-1]  # Features
y = iris_df.iloc[:, -1]   # Target (class labels)

kmeans = KMeans(n_clusters=3, random_state=42)  
kmeans.fit(X)

centroids = kmeans.cluster_centers_
print("Centroids:")
print(centroids)

labels = kmeans.labels_
print("\nLabels:")
print(labels)

# Visualizing the clusters (for 2D datasets)
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, c='red')
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
