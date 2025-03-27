import os
import zipfile
from src.load_data import DatasetFactory

DATA_FOLDER = "data/"


def detect_and_load_files(folder = DATA_FOLDER):
    """Detect and load different file types from a given folder."""
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        
        if file_name.endswith(".csv"):
            print(f"Loading CSV: {file_name}")
            loader = DatasetFactory.get_dataset_loader("csv", file_path=file_path)
            data = loader.load_data()
            print(data.head())

        elif file_name.endswith(".json"):
            print(f"Loading JSON: {file_name}")
            loader = DatasetFactory.get_dataset_loader("json", file_path=file_path)
            data = loader.load_data()
            print(data)

        elif file_name.endswith(".db"):  
            print(f"Loading SQL Database: {file_name}")
            loader = DatasetFactory.get_dataset_loader("sql", db_path=file_path, query="SELECT * FROM users")
            data = loader.load_data()
            print(data)
        else:
            print(f"Unsupported file format: {file_name}")

def main():
    detect_and_load_files()

if __name__ == "__main__":
    main()
