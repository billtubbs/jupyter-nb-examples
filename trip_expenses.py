import pandas as pd
# Trip expenses
data = {
    'Food': [38.15, 0, 109.75], 
    'Car': [139, 0, 0], 
    'Fuel': [25.08, 0, 0], 
    'Tickets': [0, 134, 0], 
    'Other': [95, 0, 250]
}
index = ['Diane', 'Kelly', 'John']
df = pd.DataFrame(data, index=index)
# Calculate amount owing
df['Total Paid'] = df.sum(axis=1)
average_cost = df['Total Paid'].mean()
df['Amounts Owing'] = average_cost - df['Total Paid']
print(df['Amounts Owing'])
