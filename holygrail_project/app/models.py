import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self, file_path='tasks.json'):
        self.file_path = file_path

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def save_tasks(self, tasks):
        with open(self.file_path, 'w') as file:
            json.dump(tasks, file, indent=4)

    def get_all_tasks(self):
        tasks = self.load_tasks()
        return sorted(tasks, key=lambda x: (x['priority'], x['due_date']))

    def add_task(self, task, due_date, priority):
        tasks = self.load_tasks()
        tasks.append({
            "task": task,
            "due_date": due_date,
            "priority": priority,
            "done": False
        })
        self.save_tasks(tasks)
        return True

    def mark_done(self, task_index):
        tasks = self.load_tasks()
        if 0 <= task_index < len(tasks):
            tasks[task_index]["done"] = True
            self.save_tasks(tasks)
            return True
        return False

    def edit_task(self, task_index, task, due_date, priority):
        tasks = self.load_tasks()
        if 0 <= task_index < len(tasks):
            tasks[task_index].update({
                "task": task,
                "due_date": due_date,
                "priority": priority
            })
            self.save_tasks(tasks)
            return True
        return False

    def delete_task(self, task_index):
        tasks = self.load_tasks()
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            self.save_tasks(tasks)
            return True
        return False 