import json
import os

def path_file(file_name = "note_book"):
    return os.path.join(os.path.dirname(__file__), f"{file_name}.txt")

def save_file(note_list: list):
    path = path_file()
    with open(path, "w", encoding="UTF-8") as file:
        json.dump(note_list, file, ensure_ascii=False)

def load_from_file():
    path = path_file()
    with open(path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data