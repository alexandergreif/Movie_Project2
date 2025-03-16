README.md
markdown
Kopieren
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
Kopieren

## GitHub Repository

You can find the code on GitHub: [Movie_Project2](https://github.com/alexandergreif/Movie_Project2)

## Requirements

- Python 3.6+
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [pytest](https://pypi.org/project/pytest/)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/alexandergreif/Movie_Project2.git
   cd Movie_Project2
(Optional) Create and activate a virtual environment:

bash
Kopieren
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
Install the required packages:

bash
Kopieren
pip install -r requirements.txt
Configure the OMDb API Key:

Create a .env file in the project root.
Add your OMDb API key in the following format:
ini
Kopieren
OMDB_API_KEY=your_api_key_here
Running the Application
Run the movie app using:

bash
Kopieren
python main.py
Running Tests
To run all tests with pytest:

bash
Kopieren
pytest
License
This project is provided for educational purposes.

yaml
Kopieren

---

### requirements.txt

requests python-dotenv pytest

yaml
Kopieren

---

These files should help set up your project on GitHub and guide others on how to run your application and tests. Let me know if you need any further adjustments!





