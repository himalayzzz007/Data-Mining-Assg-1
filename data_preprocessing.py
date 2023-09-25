import pandas as pd
from scipy.stats import zscore

# Loading the dataset
df = pd.read_csv('netflix_titles.csv')

# Data Cleaning
# Handling missing values by filling with mode
df['duration'].fillna(df['duration'].mode()[0], inplace=True)

# Converting duration to integer
df['duration'] = df['duration'].apply(lambda x: int(x.split(' ')[0]) if 'min' in x else None)

# Data Reduction
# Selecting only movies
df = df[df['type'] == 'Movie']

# Removing rows with missing duration (originally TV shows)
df.dropna(subset=['duration'], inplace=True)

# Data Normalization
df['duration'] = zscore(df['duration'])

print(df.head())

