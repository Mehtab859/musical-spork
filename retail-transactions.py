import pandas as pd
df = pd.read_csv('Retail_Transaction_Dataset.csv')
print(df.head())
print(df.describe())
print(df.info())
print(df.isnull().sum())

#Data Vis
#histplot
import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(df['TotalAmount'])
plt.title('Total Amount Distribution')
plt.show()

#Numerical variables for the heatmap
num_vars = df.drop(columns=['CustomerID']).select_dtypes(include={'number'})
sns.heatmap(num_vars)
plt.show()

plt.hist(df['DiscountApplied(%)'], bins = 20)
plt.show()

print(df['StoreLocation'].unique())

#One hot encoding
print(df['ProductCategory'].unique())
one_hot_encoder = pd.get_dummies(df['ProductCategory'])
df_encoded = pd.concat([df, one_hot_encoder], axis = 1)
print(df_encoded)

prod_df = df.drop(columns = ['ProductID'])
encoded_df = pd.concat([prod_df, one_hot_encoder], axis = 1)

prod_df['TransactionDate'] = pd.to_datetime(prod_df['TransactionDate'])
prod_df['Month'] = prod_df['TransactionDate'].dt.month
spend_by_month = df.groupby('Month')['TotalAmount'].sum()
plt.bar(spend_by_month.index, spend_by_month.values)
plt.title('Total Spend by Year')
plt.xlabel('Year')
plt.ylabel('Total Spend')
plt.xticks(spend_by_month.index)
plt.show()

encoded_df[['Books','Clothing', 'Electronics', 'Home Decor']] = encoded_df[['Books', 'Clothing', 'Electronics', 'Home Decor']].astype(int)
encoded_df = encoded_df.drop(columns=['ProductCategory'])
print(encoded_df)
sns.scatterplot(x = 'CustomerID', y = 'TotalAmount', data = encoded_df)
plt.show()
encoded_sorted = encoded_df.sort_values(by= 'TotalAmount', ascending = False)
print(encoded_sorted.head(30))

