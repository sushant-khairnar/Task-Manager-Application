import re  # Used for pattern matching (regular expressions)

# Allowed priority values
VALID_PRIORITIES = ["High", "Medium", "Low"]


# Validate string input
def validate_string(prompt, pattern=None, allow_empty=False):
    while True:
        value = input(prompt).strip()

        # Allow empty input if permitted (used in update)
        if allow_empty and value == "":
            return value

        # Check for empty input
        if not value:
            print("Input cannot be empty.")
            continue

        # Check input against regex pattern (if provided)
        if pattern and not re.match(pattern, value):
            print("Invalid format.")
            continue

        return value  # Valid input


# Validate task priority
def validate_priority(prompt):
    while True:
        value = input(prompt).strip().capitalize()

        # Check if priority is valid
        if value in VALID_PRIORITIES:
            return value

        print("Invalid priority. Please enter High, Medium, or Low.")


# Validate numeric input
def validate_number(prompt):
    try:
        return int(input(prompt))  # Convert input to integer
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
