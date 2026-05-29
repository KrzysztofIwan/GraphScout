import json

PATH = "data/user_data/user.json"

def get_user_data():
    with open(PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def set_user_data(data, key:str, new_value:str):
    data[key] = new_value
    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)