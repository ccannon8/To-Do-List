import os
import json
from datetime import datetime

def load_tasks(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_tasks(file_path, tasks):
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nTasks:")
    tasks = sorted(tasks, key=lambda x: (x['priority'], x['due_date']))
    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index + 1}. {task['task']} (Due: {task['due_date']}, Priority: {task['priority']}) - {status}")

def main():
    file_path = 'tasks.json'
    tasks = load_tasks(file_path)

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add? "))
            for _ in range(n_tasks):
                task = input("Enter the task: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                priority = int(input("Enter priority (1 = High, 2 = Medium, 3 = Low): "))
                tasks.append({"task": task, "due_date": due_date, "priority": priority, "done": False})
                print("Task added!")
            save_tasks(file_path, tasks)

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            display_tasks(tasks)
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
                save_tasks(file_path, tasks)
            else:
                print("Invalid task number.")

        elif choice == '4':
            display_tasks(tasks)
            task_index = int(input("Enter the task number to edit: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["task"] = input("Enter new task name: ")
                tasks[task_index]["due_date"] = input("Enter new due date (YYYY-MM-DD): ")
                tasks[task_index]["priority"] = int(input("Enter new priority (1 = High, 2 = Medium, 3 = Low): "))
                print("Task updated!")
                save_tasks(file_path, tasks)
            else:
                print("Invalid task number.")

        elif choice == '5':
            display_tasks(tasks)
            task_index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks.pop(task_index)
                print("Task deleted!")
                save_tasks(file_path, tasks)
            else:
                print("Invalid task number.")

        elif choice == '6':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
