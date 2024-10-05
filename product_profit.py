import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('car_data.csv')

units_sold = data['Model'].value_counts().reset_index()
units_sold.columns = ['Model', 'Units_Sold']

total_sales = data.groupby('Model')['Price'].sum().reset_index()
total_sales.columns = ['Model', 'Total_Sales']

product_data = pd.merge(total_sales, units_sold, on='Model')

product_data['Profitability'] = product_data['Total_Sales']

product_data_sorted = product_data.sort_values(by='Profitability', ascending=False)

top_performers = product_data_sorted.head(50)  
bottom_performers = product_data_sorted.tail(50)  
plt.figure(figsize=(10, 6))
sns.barplot(y='Model', x='Profitability', data=top_performers, palette='crest')
plt.title('Top Performing Car Models by Profitability')
plt.xlabel('Total Sales (Profitability)')
plt.ylabel('Car Model')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(y='Model', x='Profitability', data=bottom_performers, palette='flare')
plt.title('Worst Performing Car Models by Profitability')
plt.xlabel('Total Sales (Profitability)')
plt.ylabel('Car Model')
plt.tight_layout()
plt.show()
