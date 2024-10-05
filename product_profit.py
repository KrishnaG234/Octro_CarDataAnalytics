import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('car_data.csv')

# Calculate total units sold for each car model
units_sold = data['Model'].value_counts().reset_index()
units_sold.columns = ['Model', 'Units_Sold']

# Calculate total sales price for each car model
total_sales = data.groupby('Model')['Price'].sum().reset_index()
total_sales.columns = ['Model', 'Total_Sales']

# Merge total sales and units sold into a single DataFrame
product_data = pd.merge(total_sales, units_sold, on='Model')

# Calculate profitability
product_data['Profitability'] = product_data['Total_Sales']

# Sort the data by profitability
product_data_sorted = product_data.sort_values(by='Profitability', ascending=False)

# Split data into top and bottom performers
top_performers = product_data_sorted.head(50)  # Top 5 performing car models
bottom_performers = product_data_sorted.tail(50)  # Bottom 5 performing car models

# Plot the top performing car models
plt.figure(figsize=(10, 6))
sns.barplot(y='Model', x='Profitability', data=top_performers, palette='crest')
plt.title('Top 50 Performing Car Models by Profitability')
plt.xlabel('Total Sales (Profitability)')
plt.ylabel('Car Model')
plt.tight_layout()
plt.show()

# Plot the lowest performing car models
plt.figure(figsize=(10, 6))
sns.barplot(y='Model', x='Profitability', data=bottom_performers, palette='flare')
plt.title('Bottom 50 Performing Car Models by Profitability')
plt.xlabel('Total Sales (Profitability)')
plt.ylabel('Car Model')
plt.tight_layout()
plt.show()
