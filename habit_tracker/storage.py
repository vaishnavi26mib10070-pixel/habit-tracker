import json
import os

HABIT_FILE = "habits.json"


def load_data():
   if not os.path.exists(HABIT_FILE):
      return {"habits": [], "completions": {}}
   with open(HABIT_FILE, "r") as file:
      return json.load(file)


def save_data(data):
    with open(HABIT_FILE, "w") as file:
         json.dump(data, file, indent=2)