import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('car_data.csv')

# Inspect the first few rows and columns in the dataset
print(data.head())
print(data.columns)

# Calculate total sales price and units sold for each dealer
dealer_performance = data.groupby('Dealer_Name').agg(
    Total_Sales=('Price', 'sum'),     # Total sales price
    Units_Sold=('Dealer_Name', 'count')  # Count of car units sold
).reset_index()

# Rank dealers based on total sales price and units sold
dealer_performance['Performance_Score'] = dealer_performance['Total_Sales'] + dealer_performance['Units_Sold'] * 1000  # Weighted score for better ranking

# Sort the dealers based on performance score
dealer_performance = dealer_performance.sort_values(by='Performance_Score', ascending=False)

# Print the dealer performance summary
print(dealer_performance)

# Visualize top-performing dealers based on Total Sales
plt.figure(figsize=(12, 8))
sns.barplot(x='Total_Sales', y='Dealer_Name', data=dealer_performance.head(10), palette='coolwarm')
plt.title('Top 10 Performing Dealers by Total Sales')
plt.xlabel('Total Sales')
plt.ylabel('Dealer Name')
plt.show()

# Visualize top-performing dealers based on Units Sold
plt.figure(figsize=(12, 8))
sns.barplot(x='Units_Sold', y='Dealer_Name', data=dealer_performance.head(10), palette='Set2')
plt.title('Top 10 Dealers by Units Sold')
plt.xlabel('Units Sold')
plt.ylabel('Dealer Name')
plt.show()

# If you need a regional analysis, make sure to include region information
# Assuming 'Region' is a column in your dataset
regional_performance = data.groupby(['Dealer_Region', 'Dealer_Name']).agg({
    'Price': 'sum',
    'Dealer_Name': 'count'
}).rename(columns={'Price': 'Total_Sales', 'Dealer_Name': 'Units_Sold'}).reset_index()

# Visualize dealer performance by region
plt.figure(figsize=(10, 6))
sns.barplot(x='Total_Sales', y='Dealer_Name', hue='Dealer_Region', data=regional_performance, palette='Set2')
plt.title('Dealer Performance by Region')
plt.xlabel('Total Sales')
plt.ylabel('Dealer Name')
plt.show()
