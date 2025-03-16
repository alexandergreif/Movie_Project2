"""
StorageJson Module

This module contains the StorageJson class which implements the IStorage interface.
It uses JSON as the underlying storage format for movie data.
"""

import os
import json
from istorage import IStorage


class StorageJson(IStorage):
    """
    A JSON storage class that implements the IStorage interface.

    It provides methods for reading from and writing to a JSON file that stores movie data.
    """

    def __init__(self, file_path):
        """
        Initializes the StorageJson instance with the specified file path.

        Args:
            file_path (str): The path to the JSON file used for storage.
        """
        self.file_path = file_path

    def _read_movies(self):
        """
        Reads movie data from the JSON file.

        If the file does not exist, it is created and initialized with an empty list.
        If the file is empty or contains invalid JSON, an empty list is returned.

        Returns:
            list: A list of movie dictionaries.
        """
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as fileobj:
                json.dump([], fileobj)
        with open(self.file_path, "r") as fileobj:
            try:
                movies = json.load(fileobj)
                return movies
            except json.JSONDecodeError:
                # If file is empty or contains invalid JSON, treat it as empty.
                return []

    def _write_movies(self, movies):
        """
        Writes the provided list of movie dictionaries to the JSON file.

        Args:
            movies (list): A list of movie dictionaries to write to the file.
        """
        with open(self.file_path, "w") as fileobj:
            json.dump(movies, fileobj)

    def list_movies(self):
        """
        Reads the movie data from the JSON file and prints the details.

        Prints the total number of movies and details for each movie.
        """
        movies = self._read_movies()
        print(f"{len(movies)} movies in total")
        for movie in movies:
            print(f"{movie['title']} ({movie['year']}): {movie['rating']}")

    def add_movie(self, title, year, rating, poster):
        """
        Adds a new movie to the JSON file.

        Loads the current list of movies, appends a new movie dictionary, writes
        the updated list back to the file, and prints a confirmation message.

        Args:
            title (str): The title of the movie.
            year (int): The release year of the movie.
            rating (float): The rating of the movie.
            poster (str): The URL for the movie's poster.
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
        print(f"Movie '{title}' added successfully to the database.")

    def delete_movie(self, title):
        """
        Deletes a movie from the JSON file by its title.

        Loads the current list of movies, removes the movie whose title matches
        (case-insensitive), writes the updated list back to the file, and prints a message.

        Args:
            title (str): The title of the movie to delete.

        Returns:
            bool: True if the movie was found and deleted, False otherwise.
        """
        movies = self._read_movies()
        for movie in movies:
            if movie['title'].lower() == title.lower():
                movies.remove(movie)
                self._write_movies(movies)
                print(f"{title} has been deleted successfully.")
                return True
        print(f"No movie found matching the title {title}.")
        return False

    def update_movie(self, title, rating):
        """
        Updates the rating of an existing movie in the JSON file.

        Loads the list of movies, updates the rating for the movie with a matching title
        (case-insensitive), writes the updated list back to the file, and prints a message.

        Args:
            title (str): The title of the movie to update.
            rating (float): The new rating for the movie.

        Returns:
            bool: True if the movie was found and updated, False otherwise.
        """
        movies = self._read_movies()
        for movie in movies:
            if movie['title'].lower() == title.lower():
                movie['rating'] = rating
                self._write_movies(movies)
                print(f"Rating for {movie['title']} has been updated.")
                return True
        print(f"Movie {title} does not exist in the database.")
        return False

    def get_movies(self):
        """
        Returns the list of movies from the JSON file.

        Returns:
            list: A list of movie dictionaries.
        """
        return self._read_movies()
