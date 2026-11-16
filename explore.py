# Reflection Answers
# 1. A boolean filter evaluates a condition (True/False) for every row, and discards the Falses. 
# 2. Single brackets return a flat 1D Series, Double brackets return a structured 2D DataFrame. 
# 3. Reproducible code, identical resultes, zero hidden formula errors, handles millions of rows. 

import pandas as pd

# --- EXERCISE 1 ---

df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Dtypes:\n", df.dtypes)

# --- EXERCISE 2 ---

south = df[df['region'] == 'South']
print("South count:", len(south))
print(south.head())

# --- EXERCISE 3 ---

print(df.sort_values('revenue', ascending=False).head(5))

# --- EXERCISE 4 ---

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print("Big South count:", len(big_south))
print(big_south.head())

# --- EXERCISE 5 ---

df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print("Mean per-unit price:", df['per_unit'].mean())

# --- EXERCISE 6 ---

print("Unique regions:", df['region'].unique())
print("Region counts:\n", df['region'].value_counts())

# --- EXERCISE 7 ---

subset_df = df[['region', 'product', 'revenue']]
print("Subset shape:", subset_df.shape)

# --- EXERCISE 8 ---

df.to_csv('data/explored.csv', index=False)