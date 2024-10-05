import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('car_data.csv')

# Dealer performance by total sales and units sold
dealer_performance = data.groupby('Dealer_Name').agg(
    Total_Sales=('Price', 'sum'),         
    Units_Sold=('Dealer_Name', 'count')   
).reset_index()

# Sort by Units Sold and Total Sales
dealer_performance.sort_values(by=['Units_Sold', 'Total_Sales'], ascending=[False, False], inplace=True)

# Calculate the Performance Score
dealer_performance['Performance_Score'] = dealer_performance['Units_Sold'] + dealer_performance['Total_Sales'] / 10000 

# Display dealer performance
print(dealer_performance)

# Plot Top Performing Dealers by Combined Performance Score
plt.figure(figsize=(14, 8))
sns.barplot(x='Performance_Score', y='Dealer_Name', data=dealer_performance.head(50), palette='coolwarm')
plt.title('Top Performing Dealers by Combined Performance Score')
plt.xlabel('Combined Performance Score (Units Sold + Adjusted Total Sales)')
plt.ylabel('Dealer Name')
plt.tight_layout()  
plt.show()

# Regional performance by Dealer_Region and Dealer_Name
regional_performance = data.groupby(['Dealer_Region', 'Dealer_Name']).agg(
    Total_Sales=('Price', 'sum'),
    Units_Sold=('Dealer_Name', 'count')
).reset_index()

# Sort regional performance by region, then by Units Sold and Total Sales
regional_performance.sort_values(by=['Dealer_Region', 'Units_Sold', 'Total_Sales'], ascending=[True, False, False], inplace=True)

# Display regional performance
print(regional_performance)

# Plot 1: Top Dealers by Units Sold for each Region
plt.figure(figsize=(14, 8))
sns.barplot(x='Units_Sold', y='Dealer_Name', hue='Dealer_Region', data=regional_performance, palette='Set2')
plt.title('Top Dealers by Units Sold (Region-wise)')
plt.xlabel('Units Sold')
plt.ylabel('Dealer Name')
plt.legend(title='Region', loc='upper right')
plt.tight_layout()  
plt.show()

# Plot 2: Top Dealers by Total Sales for each Region
plt.figure(figsize=(14, 8))
sns.barplot(x='Total_Sales', y='Dealer_Name', hue='Dealer_Region', data=regional_performance, palette='Set3')
plt.title('Top Dealers by Total Sales (Region-wise)')
plt.xlabel('Total Sales')
plt.ylabel('Dealer Name')
plt.legend(title='Region', loc='upper right')
plt.tight_layout() 
plt.show()

# Plot 3: Regional performance summary (Total Sales per region)
region_sales = regional_performance.groupby('Dealer_Region').agg(Total_Sales=('Total_Sales', 'sum')).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Dealer_Region', y='Total_Sales', data=region_sales, palette='Spectral')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# Plot 4: Regional performance summary (Units Sold per region)
region_units = regional_performance.groupby('Dealer_Region').agg(Units_Sold=('Units_Sold', 'sum')).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Dealer_Region', y='Units_Sold', data=region_units, palette='Spectral')
plt.title('Units Sold by Region')
plt.xlabel('Region')
plt.ylabel('Units Sold')
plt.tight_layout()
plt.show()
