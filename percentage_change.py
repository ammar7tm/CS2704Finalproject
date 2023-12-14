import pandas as pd

# Define the dataset
data = {
    'Year': list(range(2000, 2022)),
    '18-29': [70, 72, 76, 78, 77, 83, 86, 89, 89, 92, 92, 94, 96, 97, 97, 99, 98.5, 98, 100, 99.5, 99],
    '30-49': [61, 65, 70, 72, 75, 79, 82, 85, 84, 84, 85, 87, 91, 92, 92, 95, 96, 96.5, 97, 97, 97.5, 98],
    '50-64': [46, 50, 54, 56, 61, 66, 70, 71, 72, 75, 74, 77, 79, 81, 81, 82, 87, 87, 88, 92, 96],
    '65+': [14, 14, 18, 22, 24, 28, 32, 35, 38, 40, 43, 46, 54, 56, 57, 63, 64, 65, 66, 73, 74, 75]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate the year-over-year percentage change for each age group
df.set_index('Year', inplace=True)
df_pct_change = df.pct_change().fillna(0) * 100

# Reset index to bring 'Year' back as a column
df_pct_change = df_pct_change.reset_index()

print(df_pct_change.head())
