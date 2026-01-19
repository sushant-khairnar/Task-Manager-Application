import re

VALID_PRIORITIES = ["High", "Medium", "Low"]


def validate_string(prompt, pattern=None, allow_empty=False):
    while True:
        value = input(prompt).strip()
        if allow_empty and value == "":
            return value
        if not value:
            print("Input cannot be empty.")
            continue
        if pattern and not re.match(pattern, value):
            print("Invalid format.")
            continue
        return value


def validate_priority(prompt):
    while True:
        value = input(prompt).strip().capitalize()
        if value in VALID_PRIORITIES:
            return value
        print("Invalid priority. Please enter High, Medium, or Low.")


def validate_number(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None