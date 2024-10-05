import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('car_data.csv')

# Calculate total sales price and units sold for each dealer
dealer_performance = data.groupby('Dealer_Name').agg(
    Total_Sales=('Price', 'sum'),         # Total sales price
    Units_Sold=('Dealer_Name', 'count')    # Count of car units sold
).reset_index()

# Rank dealers based on total units sold and then total sales
dealer_performance.sort_values(by=['Units_Sold', 'Total_Sales'], ascending=[False, False], inplace=True)

# Create a performance score for visualization based on both criteria
dealer_performance['Performance_Score'] = dealer_performance['Units_Sold'] + dealer_performance['Total_Sales'] / 10000  # Adjust divisor for scaling

# Print the dealer performance summary
print(dealer_performance)

# Visualize top-performing dealers based on Total Sales and Units Sold combined
plt.figure(figsize=(14, 8))
sns.barplot(x='Performance_Score', y='Dealer_Name', data=dealer_performance.head(50), palette='coolwarm')
plt.title('Top 50 Performing Dealers by Combined Performance Score')
plt.xlabel('Combined Performance Score (Units Sold + Adjusted Total Sales)')
plt.ylabel('Dealer Name')
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()

# ---- Region-wise Analysis ---- #

# Calculate total sales and units sold for each dealer by region
regional_performance = data.groupby(['Dealer_Region', 'Dealer_Name']).agg(
    Total_Sales=('Price', 'sum'),
    Units_Sold=('Dealer_Name', 'count')
).reset_index()

# Rank dealers region-wise based on total units sold, break ties by total sales
regional_performance.sort_values(by=['Dealer_Region', 'Units_Sold', 'Total_Sales'], ascending=[True, False, False], inplace=True)

# Print the regional dealer performance summary
print(regional_performance)

# Visualize regional dealer performance by units sold
plt.figure(figsize=(14, 8))
sns.barplot(x='Units_Sold', y='Dealer_Name', hue='Dealer_Region', data=regional_performance.head(10), palette='Set2')
plt.title('Top 10 Dealers by Units Sold (Region-wise)')
plt.xlabel('Units Sold')
plt.ylabel('Dealer Name')
plt.legend(title='Region')
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()

# Visualize regional dealer performance by total sales
plt.figure(figsize=(14, 8))
sns.barplot(x='Total_Sales', y='Dealer_Name', hue='Dealer_Region', data=regional_performance.head(10), palette='Set3')
plt.title('Top 10 Dealers by Total Sales (Region-wise)')
plt.xlabel('Total Sales')
plt.ylabel('Dealer Name')
plt.legend(title='Region')
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
