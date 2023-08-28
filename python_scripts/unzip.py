"""This code extracts the .rar file to the current directory."""
import os
import rarfile


def extract_rar_file(rar_file_path, extraction_path):
    try:
        # Open the RAR file
        with rarfile.RarFile(rar_file_path) as _rf:
            # Create the extraction folder if it doesn't exist
            os.makedirs(extraction_path, exist_ok=True)

            # Extract all files to the extraction folder
            _rf.extractall(extraction_path)
        print("Extraction completed successfully.")
    except Exception as exception:
        print("An error occurred:", str(exception))


if __name__ == "__main__":
    # Specify the path to the RAR file
    RAR_PATH = "data/Data.rar"

    # Specify the path where you want to extract the files
    SAVE_PATH = "data/extracted_files/"  # Change this to your desired path

    # Call the function to extract the RAR file to the specified path
    extract_rar_file(RAR_PATH, SAVE_PATH)
