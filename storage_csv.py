import os
import csv
from istorage import IStorage


class StorageCsv(IStorage):
    """
    A CSV storage class that implements the IStorage interface.
    Stores movie data in a CSV file with columns: title, year, rating, poster.
    """

    def __init__(self, file_path):
        """
        Initializes the StorageCsv instance.

        If the CSV file does not exist, creates it with a header row.

        Args:
            file_path (str): Path to the CSV file.
        """
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['title', 'year', 'rating', 'poster'])
                writer.writeheader()

    def _read_movies(self):
        """
        Reads movies from the CSV file.

        Returns:
            list: A list of dictionaries where each dictionary represents a movie.
        """
        movies = []
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert 'year' and 'rating' to proper types.
                    try:
                        row['year'] = int(row['year'])
                    except (ValueError, TypeError):
                        row['year'] = 0
                    try:
                        row['rating'] = float(row['rating'])
                    except (ValueError, TypeError):
                        row['rating'] = 0.0
                    movies.append(row)
        except FileNotFoundError:
            movies = []
        return movies

    def _write_movies(self, movies):
        """
        Writes the list of movie dictionaries to the CSV file.

        Args:
            movies (list): A list of dictionaries where each dictionary represents a movie.
        """
        with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['title', 'year', 'rating', 'poster']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for movie in movies:
                writer.writerow({
                    'title': movie['title'],
                    'year': movie['year'],
                    'rating': movie['rating'],
                    'poster': movie.get('poster', '')
                })

    def list_movies(self):
        """
        Reads the CSV file and returns a dictionary of movie information.

        Returns:
            dict: A dictionary where keys are movie titles and values are dictionaries
                  containing 'year', 'rating', and 'poster' for each movie.
        """
        movies = self._read_movies()
        movies_dict = {}
        for movie in movies:
            movies_dict[movie['title']] = {
                'year': movie['year'],
                'rating': movie['rating'],
                'poster': movie.get('poster', '')
            }
        return movies_dict

    def add_movie(self, title, year, rating, poster):
        """
        Adds a new movie to the CSV file.

        Args:
            title (str): The title of the movie.
            year (int): The release year of the movie.
            rating (float): The movie's rating.
            poster (str): URL of the movie's poster.
        """
        movies = self._read_movies()
        new_movie = {
            'title': title,
            'year': year,
            'rating': rating,
            'poster': poster
        }
        movies.append(new_movie)
        self._write_movies(movies)
        print(f"Movie '{title}' added successfully to the CSV database.")

    def delete_movie(self, title):
        """
        Deletes a movie from the CSV file by title.

        Args:
            title (str): The title of the movie to delete.

        Returns:
            bool: True if deletion was successful, False if no matching movie was found.
        """
        movies = self._read_movies()
        found = False
        updated_movies = []
        for movie in movies:
            if movie['title'].lower() == title.lower():
                found = True
            else:
                updated_movies.append(movie)
        if found:
            self._write_movies(updated_movies)
            print(f"Movie '{title}' has been deleted successfully.")
            return True
        else:
            print(f"No movie found matching the title '{title}'.")
            return False

    def update_movie(self, title, rating):
        """
        Updates the rating of a movie in the CSV file.

        Args:
            title (str): The title of the movie to update.
            rating (float): The new rating for the movie.

        Returns:
            bool: True if update was successful, False if no matching movie was found.
        """
        movies = self._read_movies()
        found = False
        for movie in movies:
            if movie['title'].lower() == title.lower():
                movie['rating'] = rating
                found = True
                break
        if found:
            self._write_movies(movies)
            print(f"Rating for movie '{title}' has been updated.")
            return True
        else:
            print(f"Movie '{title}' does not exist in the CSV database.")
            return False

    def get_movies(self):
        """
        Returns the list of movies from the CSV file.

        Returns:
            list: A list of movie dictionaries.
        """
        return self._read_movies()
