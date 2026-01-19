import json
import os
from tasks_app.task import Task

DATA_FILE = "data/tasks.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Task.from_dict(task) for task in data]
    except (json.JSONDecodeError, IOError):
        print("⚠️ Error reading tasks file. Starting with empty task list.")
        return []


def save_tasks(tasks):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)