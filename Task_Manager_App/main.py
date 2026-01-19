# Import Task class
from tasks_app.task import Task

# Import functions to load and save tasks from file
from tasks_app.file_handler import load_tasks, save_tasks

# Import input validation functions
from tasks_app.input_validator import (
    validate_string,
    validate_priority,
    validate_number
)


# Display main menu options
def display_menu():
    print("\n===== Task Manager Application =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")


# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Current Tasks:")
    # Enumerate tasks with numbering
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task.name} | {task.description} | Priority: {task.priority}")


# Add a new task
def add_task(tasks):
    print("\n--- Add New Task ---")
    # Validate user input
    name = validate_string("Enter task name: ")
    description = validate_string("Enter description: ")
    priority = validate_priority("Enter priority (High/Medium/Low): ")

    # Create and store task
    tasks.append(Task(name, description, priority))
    save_tasks(tasks)  # Save to file
    print(f"Task '{name}' added successfully!")


# Update an existing task
def update_task(tasks):
    if not tasks:
        print("No tasks available to update.")
        return

    view_tasks(tasks)
    # Get valid task index
    index = validate_number("Enter task number to update: ")
    if index is None or index < 1 or index > len(tasks):
        print("Invalid task number.")
        return

    task = tasks[index - 1]
    print("Leave blank to keep existing value.")

    # Allow empty input to keep old values
    new_name = validate_string("New name: ", allow_empty=True)
    new_desc = validate_string("New description: ", allow_empty=True)
    new_priority = input("New priority (High/Medium/Low): ").strip()

    # Update only if new values are provided
    if new_name:
        task.name = new_name
    if new_desc:
        task.description = new_desc
    if new_priority:
        task.priority = validate_priority("Confirm priority (High/Medium/Low): ")

    save_tasks(tasks)
    print(f"Task '{task.name}' updated successfully!")


# Delete a task
def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
        return

    view_tasks(tasks)
    # Select task number to delete
    index = validate_number("Enter task number to delete: ")
    if index is None or index < 1 or index > len(tasks):
        print("Invalid task number.")
        return

    # Confirmation before deletion
    confirm = input("Are you sure? (y/n): ").lower()
    if confirm == "y":
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{removed.name}' deleted successfully!")
    else:
        print("Deletion cancelled.")


# Main function (program entry point)
def main():
    tasks = load_tasks()  # Load tasks from file

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        # Menu-driven program
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run program
if __name__ == "__main__":
    main()
