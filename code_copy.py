prod_df = df.drop(columns = ['ProductID'])
encoded_df = pd.concat([prod_df, one_hot_encoder], axis = 1)
# Ensure 'TransactionDate' is in datetime format
prod_df['TransactionDate'] = pd.to_datetime(prod_df['TransactionDate'])

# Extract month from 'TransactionDate'
prod_df['Month'] = prod_df['TransactionDate'].dt.month

# Group by month and sum 'TotalAmount'
spend_by_month = prod_df.groupby('Month')['TotalAmount'].sum()

# Plot the bar chart
plt.bar(spend_by_month.index, spend_by_month.values)
plt.title('Total Spend by Month')
plt.xlabel('Month')
plt.ylabel('Total Spend')
plt.xticks(spend_by_month.index, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.show()

encoded_df[['Books','Clothing', 'Electronics', 'Home Decor']] = encoded_df[['Books', 'Clothing', 'Electronics', 'Home Decor']].astype(int)
encoded_df = encoded_df.drop(columns=['ProductCategory'])
print(encoded_df)
sns.scatterplot(x = 'CustomerID', y = 'TotalAmount', data = encoded_df)
plt.show()

customer_spend = prod_df.groupby('CustomerID')['TotalAmount'].sum()
top_customers = customer_spend.sort_values(ascending = False).head(10)
plt.figure(figsize=(10,8))
plt.bar(top_customers.index.astype(str), top_customers.values)
plt.title('Top Customers by Spend')
plt.xlabel('Customer ID')
plt.show()

bottom_customers_spend = prod_df.groupby('CustomerID')['TotalAmount'].sum()
bottom_customers = bottom_customers_spend.sort_values(ascending = False).tail(10)
plt.figure(figsize=(10,8))
plt.bar(bottom_customers.index.astype(str), bottom_customers.values)
plt.title('Bottom 10 customers by Spend')
plt.xlabel('Customer ID')
plt.show()

avg_discount = df.groupby('ProductCategory')['DiscountApplied(%)'].mean()
plt.figure(figsize=(8,6))
plt.bar(avg_discount.index, avg_discount.values)
plt.title('Average Discount by Product Category')
plt.xlabel('Category')
plt.show()


#Discount by month
discount_by_month = prod_df.groupby('Month')['DiscountApplied(%)'].mean()
plt.bar(discount_by_month.index, discount_by_month.values)
plt.title('Average Discount by Month')
plt.xlabel('Month')
plt.ylabel('Average Discount')
plt.xticks(discount_by_month.index, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.show()

max_discount_by_month = prod_df.groupby('Month')['DiscountApplied(%)'].max()
mean_discount_by_month = prod_df.groupby('Month')['DiscountApplied(%)'].mean()
max_spend_in_month = prod_df.groupby('Month')['TotalAmount'].mean()
pd.options.display.float_format = '{:,.2f}'.format 
monthly_sales = prod_df.groupby('Month')['TotalAmount'].sum()
print("Max Discounts in months: ", max_discount_by_month)
print("Average discount in months: ", mean_discount_by_month)
print("Maximum spend in month: ", max_spend_in_month)
print("Sales by months: ", monthly_sales.sort_values(ascending = False))


# Scatter plot of Discount vs. Total Spend
plt.figure(figsize=(10, 6))
plt.scatter(prod_df['DiscountApplied(%)'], prod_df['TotalAmount'], alpha=0.7)
plt.title('Correlation between Discount and Total Spend')
plt.xlabel('Discount (%)')
plt.ylabel('Total Spend ($)')
plt.grid(True)
plt.show()

# Sales by store location
store_location_sales = df.groupby('StoreLocation')['TotalAmount'].sum()
store_location_sales