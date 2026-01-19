from tasks_app.task import Task
from tasks_app.file_handler import load_tasks, save_tasks
from tasks_app.input_validator import (
    validate_string,
    validate_priority,
    validate_number
)


def display_menu():
    print("\n===== Task Manager Application =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Current Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task.name} | {task.description} | Priority: {task.priority}")


def add_task(tasks):
    print("\n--- Add New Task ---")
    name = validate_string("Enter task name: ")
    description = validate_string("Enter description: ")
    priority = validate_priority("Enter priority (High/Medium/Low): ")

    tasks.append(Task(name, description, priority))
    save_tasks(tasks)
    print(f"Task '{name}' added successfully!")


def update_task(tasks):
    if not tasks:
        print("No tasks available to update.")
        return

    view_tasks(tasks)
    index = validate_number("Enter task number to update: ")
    if index is None or index < 1 or index > len(tasks):
        print("Invalid task number.")
        return

    task = tasks[index - 1]
    print("Leave blank to keep existing value.")

    new_name = validate_string("New name: ", allow_empty=True)
    new_desc = validate_string("New description: ", allow_empty=True)
    new_priority = input("New priority (High/Medium/Low): ").strip()

    if new_name:
        task.name = new_name
    if new_desc:
        task.description = new_desc
    if new_priority:
        task.priority = validate_priority("Confirm priority (High/Medium/Low): ")

    save_tasks(tasks)
    print(f"Task '{task.name}' updated successfully!")


def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
        return

    view_tasks(tasks)
    index = validate_number("Enter task number to delete: ")
    if index is None or index < 1 or index > len(tasks):
        print("Invalid task number.")
        return

    confirm = input("Are you sure? (y/n): ").lower()
    if confirm == "y":
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{removed.name}' deleted successfully!")
    else:
        print("Deletion cancelled.")


def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

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


if __name__ == "__main__":
    main()