import pandas as pd

# Load the dataset
data = pd.read_csv('car_data.csv')

# Check for missing values
print(data.isnull().sum())

# Drop or fill missing values as necessary
data.dropna(inplace=True)  # Example: drop rows with missing values

# Display the first few rows of the dataset
print(data.head())
