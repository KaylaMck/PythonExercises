favorite_movies = []

def add_movie(movie):
    favorite_movies.append(movie)
    print(f"'{movie}' added.")

def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"'{movie}' removed.")
    else:
        print(f"'{movie}' not found.")

def display_movies():
    print("Favorite Movies:")
    for movie in favorite_movies:
        print(f"- {movie}")

def count_movies():
    count = len(favorite_movies)
    print(f"Number of movies: {count}")

def find_movie(movie):
    if movie in favorite_movies:
        print (f"'{movie}' found.")
    else:
        print (f"'{movie}' not found.")

def clear_movies():
    favorite_movies.clear()
    print("All movies have been removed from list.")

print("\n--- Testing add_movie() ---")
add_movie("The Shawshank Redemption")
add_movie("The Godfather")
add_movie("Pulp Fiction")