import movies

#for testing helper functions
ironman_movie = ["Iron Man 3", 1.214, 2013, 7.0, 325]

print(movies.get_name(ironman_movie))
print(movies.get_gross(ironman_movie))
print(movies.get_rating(ironman_movie))
print(movies.get_num_ratings(ironman_movie))
print()

#for testing better_movies and averages
movies_lst = [
    #name, gross from box office, year, rating, num_reviews
    ["Avengers: Endgame", 2.797, 2019, 8.2, 532],
    ["Avengers: Infinity War", 2.048, 2018, 7.6, 474],
    ["The Avengers", 1.518, 2012, 8.0, 358],
    ["Avengers: Age of Ultron", 1.405, 2015, 6.8, 370],
    ["Black Panther", 1.346, 2018, 8.3, 515],
    ["Incredibles 2", 1.242, 2018, 7.84, 379],
    ["Iron Man 3", 1.214, 2013, 7.0, 325]
]
result = movies.better_movies("Iron Man 3", movies_lst)
for movie in result:
    print(movie)
print()
print(movies.average("rating", movies_lst))
print(movies.average("gross", movies_lst))
print(movies.average("number of ratings", movies_lst))