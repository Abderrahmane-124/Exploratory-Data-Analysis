import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données
data = pd.read_csv('amazon.csv')

# Top 5 des meilleures catégories
print("Top 5 des meilleures catégories:")
top_categories = data['listed_in'].value_counts().head(5)
print(top_categories)
top_categories.plot(kind='bar')
plt.title('Top 5 des meilleures catégories')
plt.show()


# Top 5 des réalisateurs
print("########################################################################################################")
print("Top 5 des réalisateurs:")
top_directors = data['director'].value_counts().head(5)
print(top_directors)
top_directors.plot(kind='bar')
plt.title('Top 5 des réalisateurs')
plt.show()

# Les dix meilleurs acteurs
print("########################################################################################################")
print("Les dix meilleurs acteurs:")
top_actors = data['cast'].value_counts().head(10)
print(top_actors)
top_actors.plot(kind='bar')
plt.title('Les dix meilleurs acteurs')
plt.show()

# Les cinq meilleures séries télévisées avec le plus grand nombre de saisons
print("########################################################################################################")
print("Les cinq meilleures séries télévisées avec le plus grand nombre de saisons:")
top_shows = data[data['type'] == 'TV Show']['duration'].value_counts().head(5)
print(top_shows)
top_shows.plot(kind='bar')
plt.title('Les cinq meilleures séries télévisées avec le plus grand nombre de saisons')
plt.show()

# Amazon se concentre-t-il davantage sur les séries télévisées que sur les films ces dernières années ?
print("########################################################################################################")
print("Amazon se concentre-t-il davantage sur les séries télévisées que sur les films ces dernières années?")
recent_data = data[data['release_year'] > 2015]
tv_vs_movies = recent_data['type'].value_counts()
print(tv_vs_movies)
tv_vs_movies.plot(kind='bar')
plt.title('Amazon se concentre-t-il davantage sur les séries télévisées que sur les films ces dernières années ?')
plt.show()



