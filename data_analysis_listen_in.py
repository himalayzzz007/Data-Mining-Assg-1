'''
The “listed_in” attribute is a categorical variable that represents the genre(s) of a movie or TV show.

For categorical data, we typically use the mode as a measure of central tendency, which represents the most common genre(s) in the dataset.

For dispersion, we can calculate the number of unique genres.

A bar chart would be an appropriate visualization technique for this attribute, showing the count of each genre.
'''

import pandas as pd
import matplotlib.pyplot as plt

# Loading the dataset
df = pd.read_csv('netflix_titles.csv')

# Splitting the genres and expanding them into separate rows
genres = df['listed_in'].str.split(', ').apply(pd.Series).stack().reset_index(drop=True)

# Measure of Central Tendency
mode = genres.mode()[0]

# Measure of Dispersion
unique_genres = genres.nunique()

print(f"Mode: {mode}")
print(f"Number of unique genres: {unique_genres}")

# Preparing data for visualization
top_10_genres = genres.value_counts()[:10]
other_genres = pd.Series([genres.value_counts()[10:].sum()], index=['Others'])
genres_to_plot = pd.concat([top_10_genres, other_genres])

# Visualization
genres_to_plot.plot(kind='pie', figsize=(10,10), autopct='%1.1f%%')
plt.title('Distribution of Genres')
plt.show()

