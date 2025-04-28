import os

def get_tasks_file():
    return os.getenv("TASKS_FILE_PATH", "tasks.json")
