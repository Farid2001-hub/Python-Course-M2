import unittest
import os
import json
from task_manager.core import add_task, load_tasks, delete_task
from task_manager.config import get_tasks_file

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Utiliser un fichier temporaire pour les tests
        self.test_tasks_file = "test_tasks.json"
        os.environ["TASKS_FILE_PATH"] = self.test_tasks_file
        if os.path.exists(self.test_tasks_file):
            os.remove(self.test_tasks_file)

    def tearDown(self):
        if os.path.exists(self.test_tasks_file):
            os.remove(self.test_tasks_file)

    def test_add_task(self):
        task = add_task("Test Task", 2)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['description'], "Test Task")
        self.assertEqual(tasks[0]['priority'], 2)

    def test_delete_task(self):
        add_task("Task to Delete", 1)
        tasks = load_tasks()
        task_id = tasks[0]["id"]
        result = delete_task(task_id)
        self.assertTrue(result)
        tasks_after = load_tasks()
        self.assertEqual(len(tasks_after), 0)

if __name__ == "__main__":
    unittest.main()
