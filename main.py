from storage_csv import StorageCsv
from storage_json import StorageJson
from movie_app import MovieApp

def main():
    """
    Main function that initializes the storage and the MovieApp,
    then starts the application by calling its run() method.
    """
    storage = StorageJson("storage.json")
    #storage = StorageCsv("storage.csv")
    app = MovieApp(storage)
    app.run()

if __name__ == "__main__":
    main()
