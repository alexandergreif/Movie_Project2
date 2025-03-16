# Movie App

Movie App is a command-line and web-based application to manage a movie database. It allows users to add movies manually or via the OMDb API, delete and update movies, list movies, and generate a website to display the movie collection.

## Features

- **Manual Movie Addition:** Enter movie details (title, release year, rating, poster URL) manually.
- **OMDb API Integration:** Add movies by entering just the title. The app fetches details (Title, Year, IMDb Rating, Poster URL) from the OMDb API.
- **CRUD Operations:** List, update, and delete movies from your collection.
- **Multiple Storage Options:** Data can be stored using JSON or CSV storage.
- **Website Generation:** Generate an HTML website using a template to display all movies in a grid.

## Project Structure

. ├── istorage.py # IStorage interface definition ├── storage_json.py # JSON storage implementation ├── storage_csv.py # CSV storage implementation ├── movie_app.py # CLI app containing all commands (CRUD, website generation, etc.) ├── main.py # Main entry point of the application ├── omdb_client.py # Module for interacting with the OMDb API ├── _static │ ├── index_template.html # HTML template for website generation │ └── style.css # CSS file for styling the website ├── README.md # Project documentation └── requirements.txt # List of required packages

markdown


## Requirements

- Python 3.6+
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [pytest](https://pypi.org/project/pytest/)

## Setup Instructions

1. **(Optional) Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
Install Dependencies:

bash

pip install -r requirements.txt
Create a .env File for OMDb API Key:

ini

OMDB_API_KEY=your_api_key_here
Running the Application
bash

python main.py
Running Tests
To run all tests with pytest:

bash

pytest
License
This project is provided for educational purposes.



---

This updated README removes the “yaml ” references and keeps the instructions concise. If you need further modifications or want to include additional information, feel free to edit accordingly!





