'''
The “cast” attribute is a categorical variable that represents the cast of a movie or TV show.

For categorical data, we typically use the mode as a measure of central tendency, which represents the most common actor(s) in the dataset.

For dispersion, we can calculate the number of unique actors.

A bar chart would be an appropriate visualization technique for this attribute, showing the count of each actor.
'''

import pandas as pd
import matplotlib.pyplot as plt

# Loading the dataset
df = pd.read_csv('netflix_titles.csv')

# Splitting the cast and expanding them into separate rows
cast = df['cast'].dropna().str.split(', ').apply(pd.Series).stack().reset_index(drop=True)

# Measure of Central Tendency
mode = cast.mode()[0]

# Measure of Dispersion
unique_cast = cast.nunique()

print(f"Mode: {mode}")
print(f"Number of unique actors: {unique_cast}")

# Visualization
cast.value_counts()[:30].plot(kind='bar', figsize=(12,6))  # Displaying top 30 for readability
plt.title('Distribution of Actors')
plt.xlabel('Actor')
plt.ylabel('Count')
plt.show()

