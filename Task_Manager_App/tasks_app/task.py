class Task:
    # Constructor to initialize task details
    def __init__(self, name, description, priority):
        self.name = name            # Task title
        self.description = description  # Task details
        self.priority = priority    # Task priority (High/Medium/Low)

    # Convert Task object to dictionary (used for file storage)
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "priority": self.priority
        }

    # Create Task object from dictionary data
    @staticmethod
    def from_dict(data):
        return Task(
            data.get("name", ""),         # Get task name
            data.get("description", ""),  # Get description
            data.get("priority", "")      # Get priority
        )
