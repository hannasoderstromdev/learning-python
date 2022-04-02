from movie import Movie
from user import User

my_movie = Movie('The Matrix', 'Sci-fi', True)

user = User("Hanna")

user.movies.append(my_movie)

print(user.name, user.movies_watched())