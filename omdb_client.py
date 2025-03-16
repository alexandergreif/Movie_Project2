"""
omdb_client.py

This module provides functions to interact with the OMDb API. It loads the API key from a
.env file and defines functions to fetch movie details by title and search for movies by query.
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OMDb API key from the environment
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
if not OMDB_API_KEY:
    raise ValueError("OMDB_API_KEY not set in .env file")

# Base URL for the OMDb API
BASE_URL = "http://www.omdbapi.com/"


def get_movie_by_title(title):
    """
    Fetch movie details by title using the OMDb API.

    Args:
        title (str): The title of the movie to retrieve.

    Returns:
        dict: A dictionary containing movie details from the API response.
              If the movie is not found, the API typically returns a response with
              'Response': 'False' and an 'Error' message.
    """
    params = {
        "apikey": OMDB_API_KEY,
        "t": title
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()


def search_movies(query):
    """
    Search for movies matching the given query using the OMDb API.

    Args:
        query (str): The search query for movies.

    Returns:
        dict: A dictionary containing search results from the API response.
              It includes a list of movies under the 'Search' key if successful.
    """
    params = {
        "apikey": OMDB_API_KEY,
        "s": query
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()
