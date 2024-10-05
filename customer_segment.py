import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

# Load the dataset
data = pd.read_csv('car_data.csv')

# Select relevant columns
customer_data = data[['Customer Name', 'Gender', 'Annual Income']]

# Map Gender column to numeric values
customer_data['Gender'] = customer_data['Gender'].map({'Male': 0, 'Female': 1})

# Apply KMeans clustering based on 'Annual Income'
kmeans = KMeans(n_clusters=3)
customer_data['Segment'] = kmeans.fit_predict(customer_data[['Annual Income']])

# Plot 1: Scatterplot of Annual Income vs Segment with larger, more visible dots
plt.figure(figsize=(12, 8))  # Adjusted figure size for better visibility
sns.scatterplot(x='Annual Income', y='Segment', hue='Segment', data=customer_data, 
                palette='viridis', s=100, edgecolor='black', linewidth=0.5)

plt.title('Customer Segmentation based on Annual Income', fontsize=16)
plt.xlabel('Annual Income', fontsize=14)
plt.ylabel('Customer Segment', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)  # Add grid for better readability
plt.tight_layout()  # Ensure labels and title fit well within the figure
plt.show()

# Summary of segments (Mean Annual Income per segment)
segment_summary = customer_data.groupby('Segment').agg({'Annual Income': 'mean'}).reset_index()
print(segment_summary)

# Plot 2: Barplot of Customer Segment Distribution
segment_counts = customer_data['Segment'].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=segment_counts.index, y=segment_counts.values, palette='viridis')
plt.title('Customer Segment Distribution', fontsize=16)
plt.xlabel('Segment', fontsize=14)
plt.ylabel('Number of Customers', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()

# Plot 3: Boxplot of Income Distribution by Segment
plt.figure(figsize=(10, 6))
sns.boxplot(x='Segment', y='Annual Income', data=customer_data, palette='viridis')
plt.title('Income Distribution Across Customer Segments', fontsize=16)
plt.xlabel('Customer Segment', fontsize=14)
plt.ylabel('Annual Income', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()

# Plot 4: Scatterplot of Annual Income vs Segment (same as Plot 1 but kept for clarity)
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Annual Income', y='Segment', hue='Segment', palette='viridis', data=customer_data, s=100, edgecolor='black', linewidth=0.5)
plt.title('Customer Segmentation based on Annual Income', fontsize=16)
plt.xlabel('Annual Income', fontsize=14)
plt.ylabel('Customer Segment', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()
