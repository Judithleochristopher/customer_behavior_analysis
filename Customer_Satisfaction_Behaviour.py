import pandas as pd
df=pd.read_csv('customer_shopping_behaviorfile.csv')
print(df.head())
print(df.info())
print(df.describe(include='all'))
df.isnull().sum()


