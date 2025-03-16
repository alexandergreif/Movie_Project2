from istorage import IStorage
from omdb_client import get_movie_by_title  # Import our OMDb API function


def get_int(prompt):
    """
    Prompts the user to enter an integer and validates the input.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_float(prompt):
    """
    Prompts the user to enter a float and validates the input.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        float: The float value entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_str(prompt):
    """
    Prompts the user to enter a string.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        str: The string entered by the user.
    """
    return input(prompt).strip()


class MovieApp:
    """
    MovieApp class that encapsulates the CLI logic for the movie application.

    It uses an IStorage instance for performing CRUD operations on movie data.
    """

    def __init__(self, storage: IStorage):
        """
        Initializes the MovieApp with the given storage instance.

        Args:
            storage (IStorage): An instance that implements the IStorage interface.
        """
        self._storage = storage

    def _command_list_movies(self):
        """
        Lists all movies stored in the storage.
        """
        movies = self._storage.get_movies()
        if movies:
            print(f"{len(movies)} movies in total:")
            for movie in movies:
                print(f"{movie['title']} ({movie['year']}): {movie['rating']}")
        else:
            print("No movies in the database.")

    def _command_add_movie_manual(self):
        """
        Adds a new movie to the storage manually.

        Prompts the user for all movie details (title, release year, rating, poster URL)
        and then saves the movie.
        """
        title = get_str("Enter movie title: ")
        year = get_int("Enter release year: ")
        rating = get_float("Enter rating: ")
        poster = get_str("Enter poster URL (or leave blank): ")
        self._storage.add_movie(title, year, rating, poster)
        print("Movie added successfully (manual entry).")

    def _command_add_movie_api(self):
        """
        Adds a new movie by fetching details from the OMDb API.

        Prompts the user for the movie title, then fetches the movie's details
        (Title, Year, Rating, and Poster URL) from the OMDb API.
        If the movie is found, it is added to the storage. Errors are handled
        for missing movies or connection issues.
        """
        title = get_str("Enter movie title: ")
        try:
            movie_data = get_movie_by_title(title)
        except Exception as e:
            print(f"Error fetching data from OMDb API: {e}")
            return

        if movie_data.get("Response", "False") == "False":
            print(f"Movie '{title}' not found in OMDb API. Please try another title.")
            return

        movie_title = movie_data.get("Title", title)
        movie_year = movie_data.get("Year", "0")
        movie_rating = movie_data.get("imdbRating", "0")
        movie_poster = movie_data.get("Poster", "")

        try:
            movie_year = int(movie_year)
        except ValueError:
            movie_year = 0

        try:
            movie_rating = float(movie_rating)
        except ValueError:
            movie_rating = 0.0

        self._storage.add_movie(movie_title, movie_year, movie_rating, movie_poster)
        print(f"Movie '{movie_title}' added successfully (via OMDb API).")

    def _command_delete_movie(self):
        """
        Deletes a movie from the storage.
        """
        title = get_str("Enter movie title to delete: ")
        if self._storage.delete_movie(title):
            print("Movie deleted successfully.")
        else:
            print("Movie not found.")

    def _command_update_movie(self):
        """
        Updates the rating of a movie in the storage.
        """
        title = get_str("Enter movie title to update: ")
        rating = get_float("Enter new rating: ")
        if self._storage.update_movie(title, rating):
            print("Movie updated successfully.")
        else:
            print("Movie not found.")

    def _command_generate_website(self):
        """
        Generates a website using an HTML template.

        Reads the template file from _static/index_template.html, replaces the placeholders:
        __TEMPLATE_TITLE__ with the website title and __TEMPLATE_MOVIE_GRID__ with HTML for
        each movie. The resulting HTML is written to index.html.
        """
        template_path = "_static/index_template.html"
        output_path = "index.html"

        # Read the template file
        try:
            with open(template_path, "r", encoding="utf-8") as file:
                template = file.read()
        except FileNotFoundError:
            print("Template file not found.")
            return

        # Set website title (you can change this as desired)
        website_title = "My Movie App"

        # Build movie grid HTML by iterating over movies from storage
        movies = self._storage.get_movies()
        movie_grid = ""
        for movie in movies:
            movie_item = (
                f'<div class="movie">\n'
                f'  <img src="{movie.get("poster", "")}" alt="{movie["title"]} poster">\n'
                f'  <h2>{movie["title"]}</h2>\n'
                f'  <p>Year: {movie["year"]}</p>\n'
                f'  <p>Rating: {movie["rating"]}</p>\n'
                f'</div>\n'
            )
            movie_grid += movie_item

        # Replace the placeholders in the template
        template = template.replace("__TEMPLATE_TITLE__", website_title)
        template = template.replace("__TEMPLATE_MOVIE_GRID__", movie_grid)

        # Write the generated website to index.html
        try:
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(template)
            print("Website was generated successfully.")
        except Exception as e:
            print(f"Error writing website file: {e}")

    def _exit_app(self):
        """
        Exits the MovieApp.
        """
        print("Exiting Movie App. Thank you!")

    def run(self):
        """
        Runs the MovieApp, displaying a menu and processing user commands until exit.
        """
        # Updated command dictionary to follow the instructions:
        # "0: Exit", "1: List Movies", ..., "9: Generate website"
        commands = {
            "1": self._command_list_movies,
            "2": self._command_add_movie_manual,
            "3": self._command_delete_movie,
            "4": self._command_update_movie,
            "5": self._command_add_movie_api,
            "9": self._command_generate_website,
            "0": self._exit_app,
        }

        while True:
            print("\nMovie App Menu:")
            print("0. Exit")
            print("1. List Movies")
            print("2. Add Movie (manual)")
            print("3. Delete Movie")
            print("4. Update Movie")
            print("5. Add Movie (via OMDb API)")
            print("9. Generate website")

            choice = get_str("Choose an option: ")
            if choice in commands:
                commands[choice]()  # Call the corresponding function
                if choice == "0":  # Exit option
                    break
            else:
                print("Invalid choice, please try again.")
            input("Press Enter to continue...")
