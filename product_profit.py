import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('car_data.csv')

# Check the first few rows and columns in the dataset
print(data.head())
print(data.columns)

# Calculate total units sold for each car model
# This counts the number of occurrences for each Model
units_sold = data['Model'].value_counts().reset_index()
units_sold.columns = ['Model', 'Units_Sold']

# Calculate total sales price for each car model
# Sum the price for each Model
total_sales = data.groupby('Model')['Price'].sum().reset_index()
total_sales.columns = ['Model', 'Total_Sales']

# Merge total sales and units sold into a single DataFrame
product_data = pd.merge(total_sales, units_sold, on='Model')

# Calculate profitability
product_data['Profitability'] = product_data['Total_Sales']  # Total sales can be considered as profitability for simplicity

# Visualization of profitability by car model
# Visualization of profitability by car model
plt.figure(figsize=(14, 7))  # Adjust figure size if needed
sns.barplot(x='Model', y='Profitability', data=product_data, palette='crest')

# Rotate labels to prevent overlap
plt.xticks(rotation=45, ha='right')  # Rotate and align labels to the right
plt.title('Profitability by Car Model')
plt.xlabel('Car Model')
plt.ylabel('Total Sales (Profitability)')
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()

