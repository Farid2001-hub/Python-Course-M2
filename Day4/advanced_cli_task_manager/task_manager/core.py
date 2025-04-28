import json
import os
from task_manager.logger import setup_logger
from task_manager.config import get_tasks_file

logger = setup_logger()

def load_tasks():
    tasks_file = get_tasks_file()
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    tasks_file = get_tasks_file()
    with open(tasks_file, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description, priority):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "priority": priority
    }
    tasks.append(task)
    save_tasks(tasks)
    logger.info(f"Added task: {task}")
    return task

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        print(f"ID: {task['id']} | Priority: {task['priority']} | Description: {task['description']}")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(updated_tasks) == len(tasks):
        logger.warning(f"Task ID {task_id} not found.")
        return False
    save_tasks(updated_tasks)
    logger.info(f"Deleted task ID: {task_id}")
    return True
