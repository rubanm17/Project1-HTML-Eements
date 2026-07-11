import pandas as pd
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt



df = pd.read_csv("movies.csv")



df = df.dropna()
df = df[df["title"] != "unknown"]



df["title_clean"] = df["title"].str.lower()



all_words = []

for title in df["title_clean"]:
    words = title.split()
    for word in words:
        if word not in all_words:
            all_words.append(word)



def create_vector(title):
    vector = []

    words = title.split()

    for word in all_words:
        vector.append(words.count(word))

    return np.array(vector)



vectors = {}

for index, row in df.iterrows():
    vectors[row["title"]] = create_vector(row["title_clean"])




def cosine_similarity(vec1, vec2):

    dot_product = np.dot(vec1, vec2)

    magnitude1 = sqrt(np.sum(vec1 ** 2))
    magnitude2 = sqrt(np.sum(vec2 ** 2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    return dot_product / (magnitude1 * magnitude2)




def recommend(movie_name, top_n=5):

    if movie_name not in vectors:
        return "Movie not found"

    movie_vector = vectors[movie_name]

    similarity_list = []


    for movie, vector in vectors.items():

        if movie != movie_name:

            score = cosine_similarity(
                movie_vector,
                vector
            )

            similarity_list.append(
                (movie, score)
            )


    similarity_list.sort(
        key=lambda x:x[1],
        reverse=True
    )


    return similarity_list[:top_n]




movie = "Toy Story (1995)"

results = recommend(movie,5)


print("Recommended Movies:")

for movie, score in results:
    print(movie, "-> Similarity:", round(score,3))



movies = []
scores = []

for movie, score in results:
    movies.append(movie[:20])
    scores.append(score)


plt.figure(figsize=(10,5))

plt.bar(
    movies,
    scores
)

plt.xticks(rotation=45)

plt.xlabel("Movies")

plt.ylabel("Similarity Score")

plt.title("Movie Recommendation Similarity")

plt.show()