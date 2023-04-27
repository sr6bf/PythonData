#sr6bf Sarah Raza

#helper functions
def get_name(movie):
    '''
    :param movie: movie takes in a parameter for the movie list
    :return: Returns the name in the provided list
    '''
    return movie[0]

def get_gross(movie):
    '''
    :param movie: movie takes in a parameter for the movie list
    :return: Return the gross earnings in the
    '''
    return movie[1]

def get_rating(movie):
    '''
    :param movie: movie takes in a parameter for the movie list
    :return: Returns the rating in the provided list
    '''
    return movie[3]

def get_num_ratings(movie):
    '''
    :param movie: movie takes in a parameter for the movie list
    :return: Returns the number of ratings in the provided list
    '''
    return movie[4]

#main functions

def better_movies(movie_name,movies_list):
    '''
    :param movie_name: Takes in a string parameter whose value corresponds to the movie name in movies_list
    :param movies_list: Takes in a parameter for a list of lists, where the list inside the larger list contains a movie's information
    :return: This function takes the provided movie_name and searches through the provided movies_list and returns a list of all movies' information that have a higher rating than that of movie_name
    '''
    better_ratings = []
    rating = 0
    for movie in movies_list:
     if get_name(movie) == movie_name:
        rating = get_rating(movie)
    for movie in movies_list:
     if get_rating(movie) > rating:
        better_ratings.append(movie)
    return better_ratings

def average(category,movies_list):
    '''
    :param category: Takes in a string parameter whose value will either be "rating","gross","or "number of ratings"
    :param movies_list: Takes in a list of lists, where the lists inside the larger list contain a movie's information
    :return: This function returns the average for all movies based on the provided category
    '''
    total = 0
    count = 0
    for movie in movies_list:
        if category == 'rating':
            total += get_rating(movie)
            count += 1
        elif category == 'gross':
            total += get_gross(movie)
            count += 1
        elif category == 'number of ratings':
            total += get_num_ratings(movie)
            count += 1
    return total / count

