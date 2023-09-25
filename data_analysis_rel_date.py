'''
The measures of central tendency we can calculate are:

Mean: It gives the average release year of all the movies and TV shows.
Median: It gives the middle point of release years.
The measures of dispersion we can calculate are:

Range: It gives the difference between the oldest and the latest release year.
Variance and Standard Deviation: These give us an idea of how spread out the release years are.
For visualization, a histogram would be appropriate as it can show the distribution of release years.
'''


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset
df = pd.read_csv('netflix_titles.csv')

# Convert the "date_added" column to a datetime data type
#df['date_added'] = pd.to_datetime(df['date_added'])
df['director']=df['director'].fillna('No Data Available')        
df['cast']=df['cast'].fillna('No Data Available')              
df['country']=df['country'].fillna(df['country'].mode()[0])     
df['date_added']=df['date_added'].fillna(df['date_added'].mode()[0])          
df['rating']=df['rating'].fillna(df['rating'].mode()[0])               
df['duration']=df['director'].fillna('No Data Available')  

# Measures of Central Tendency
mean = df['release_year'].mean()
median = df['release_year'].median()

# Measures of Dispersion
range_ = df['release_year'].max() - df['release_year'].min()
variance = df['release_year'].var()
std_dev = df['release_year'].std()

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Range: {range_}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")

# Visualization
plt.hist(df['release_year'], bins=30, edgecolor='black')
plt.title('Distribution of Release Years')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.show()

