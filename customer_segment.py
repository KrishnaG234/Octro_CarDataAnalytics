import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd


data = pd.read_csv('car_data.csv')
# Select relevant columns for segmentation
customer_data = data[['Customer Name', 'Gender', 'Annual Income']]  # Adjust columns as necessary

# Encode categorical variables if needed
customer_data['Gender'] = customer_data['Gender'].map({'Male': 0, 'Female': 1})

# K-means clustering for customer segmentation
kmeans = KMeans(n_clusters=3)  # Adjust number of clusters as needed
customer_data['Segment'] = kmeans.fit_predict(customer_data[['Annual Income']])

# Visualize customer segments
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Annual Income', y='Segment', hue='Segment', data=customer_data, palette='viridis')
plt.title('Customer Segmentation based on Annual Income')
plt.xlabel('Annual Income')
plt.ylabel('Customer Segment')
plt.show()

# Summary of customer segments
segment_summary = customer_data.groupby('Segment').agg({'Annual Income': 'mean'}).reset_index()
print(segment_summary)
