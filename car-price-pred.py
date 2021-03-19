import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


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
## Convert to one hot encoded
final_dataset=pd.get_dummies(final_dataset, drop_first=True)
print(final_dataset.head())

######################## A handy way To display columns fully #############
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)
###########################################################################
corrmat = final_dataset.corr()
top_corr_features = corrmat.index
print(top_corr_features) ## shows correlation
plt.figure(figsize=(20,20))
# sns.pairplot(final_dataset)
# plt.show()
## plot heatmap
g = sns.heatmap(final_dataset[top_corr_features].corr(), annot=True, cmap='RdYlGn')
plt.show()

X = final_dataset.iloc