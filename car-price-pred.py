import pandas as pd
df = pd.read_csv('car data.csv')
print(df.head())
print(df.shape)
print(df['Seller_Type'].unique())
print(df['Transmission'].unique())
print(df['Owner'].unique())
## check missing or null values
print(df.isnull().sum())
print(df.describe())
print(df.columns)
final_dataset = df[['Year', 'Selling_Price', 'Present_Price', 'Kms_Driven',
       'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']]
print(final_dataset.columns)
final_dataset['Current_Year']=2020
final_dataset['no_year'] = final_dataset['Current_Year'] - final_dataset['Year']
print(final_dataset.head())
final_dataset.drop(['Year','Current_Year'], axis=1, inplace=True)
print(final_dataset.head())
