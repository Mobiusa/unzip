import zipfile
import argparse
import os

def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Unzip a file to a specified directory.')
    parser.add_argument('zip_path', type=str, help='Path to the zip file.')
    parser.add_argument('extract_to', type=str, help='Directory to extract the contents to.')

    args = parser.parse_args()

    # Ensure the extract_to directory exists
    if not os.path.exists(args.extract_to):
        os.makedirs(args.extract_to)

    unzip_file(args.zip_path, args.extract_to)
