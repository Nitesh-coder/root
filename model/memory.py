import json
import os


def store(data):
    file_path = "db/timeflow.json"
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    try:
        with open(file_path, "r") as file:
            read_data = json.load(file)
        
        if "timeflow" not in read_data:
            read_data["timeflow"] = []
        
        read_data["timeflow"].append(data)
        
    except FileNotFoundError:
        print("File not found! Creating a new one...")
        read_data = {"timeflow": [data]}
    
    
    with open(file_path, "w") as file:
        json.dump(read_data, file, indent=4)
    print("Data saved successfully.")
