import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('car_data.csv')

dealer_performance = data.groupby('Dealer_Name').agg(
    Total_Sales=('Price', 'sum'),         
    Units_Sold=('Dealer_Name', 'count')   
).reset_index()

dealer_performance.sort_values(by=['Units_Sold', 'Total_Sales'], ascending=[False, False], inplace=True)

dealer_performance['Performance_Score'] = dealer_performance['Units_Sold'] + dealer_performance['Total_Sales'] / 10000 

print(dealer_performance)

plt.figure(figsize=(14, 8))
sns.barplot(x='Performance_Score', y='Dealer_Name', data=dealer_performance.head(50), palette='coolwarm')
plt.title('Top Performing Dealers by Combined Performance Score')
plt.xlabel('Combined Performance Score (Units Sold + Adjusted Total Sales)')
plt.ylabel('Dealer Name')
plt.tight_layout()  
plt.show()


regional_performance = data.groupby(['Dealer_Region', 'Dealer_Name']).agg(
    Total_Sales=('Price', 'sum'),
    Units_Sold=('Dealer_Name', 'count')
).reset_index()

regional_performance.sort_values(by=['Dealer_Region', 'Units_Sold', 'Total_Sales'], ascending=[True, False, False], inplace=True)

print(regional_performance)

plt.figure(figsize=(14, 8))
sns.barplot(x='Units_Sold', y='Dealer_Name', hue='Dealer_Region', data=regional_performance.head(10), palette='Set2')
plt.title('Top 10 Dealers by Units Sold (Region-wise)')
plt.xlabel('Units Sold')
plt.ylabel('Dealer Name')
plt.legend(title='Region')
plt.tight_layout()  
plt.show()

plt.figure(figsize=(14, 8))
sns.barplot(x='Total_Sales', y='Dealer_Name', hue='Dealer_Region', data=regional_performance.head(10), palette='Set3')
plt.title('Top 10 Dealers by Total Sales (Region-wise)')
plt.xlabel('Total Sales')
plt.ylabel('Dealer Name')
plt.legend(title='Region')
plt.tight_layout() 
plt.show()
