import json      # Used for reading and writing JSON files
import os        # Used for file and directory operations
from tasks_app.task import Task  # Import Task class

# File path to store tasks
DATA_FILE = "data/tasks.json"


# Load tasks from JSON file
def load_tasks():
    # If file does not exist, return empty list
    if not os.path.exists(DATA_FILE):
        return []

    try:
        # Open and read JSON file
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            # Convert dictionary data to Task objects
            return [Task.from_dict(task) for task in data]

    # Handle file read or JSON format errors
    except (json.JSONDecodeError, IOError):
        print("⚠️ Error reading tasks file. Starting with empty task list.")
        return []


# Save tasks to JSON file
def save_tasks(tasks):
    # Create data directory if it does not exist
    os.makedirs("data", exist_ok=True)

    # Write task data to JSON file
    with open(DATA_FILE, "w") as f:
        json.dump(
            [task.to_dict() for task in tasks],  # Convert objects to dict
            f,
            indent=4  # Pretty JSON formatting
        )
