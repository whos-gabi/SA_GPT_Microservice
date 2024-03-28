import os
import json
from pymongo import MongoClient
import certifi


def upload_to_mongo(json_file_path):
    # Load JSON data from file
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    print(json_file_path)
    # Connect to MongoDB    
    client = MongoClient("mongodb+srv://admin:studentapp1234@cluster0.84x1ogu.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
    print(client)
    db = client['student-app']

    # Insert data into the 'chapters' collection
    collection = db['subjects_curriculum']
    collection.insert_one(data['course'])

    print(f"Uploaded data from {json_file_path} to MongoDB.")

def main():
    # Specify the directory containing JSON files
    directory = 'chapters_db/'

    # Loop through JSON files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            upload_to_mongo(file_path)

if __name__ == "__main__":
    main()
