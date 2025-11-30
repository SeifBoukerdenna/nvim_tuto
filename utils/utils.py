import json
import os

NAME_OF_FILE = "tasks.json"


class TaskHandler:
    def __init__(self):
        if not os.path.exists(NAME_OF_FILE):
            with open(NAME_OF_FILE, "w") as f:
                json.dump([], f)

    def list_task(self):
        with open(NAME_OF_FILE, "r") as f:
            data = json.load(f)

        for idx, item in enumerate(data):
            print(f"{idx + 1}. {item['task']} [{item['status']}]")

    def add_task(self, task):
        with open(NAME_OF_FILE, "r") as f:
            data = json.load(f)

        data.append({"task": task, "status": "pending"})

        with open(NAME_OF_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Added: {task}")
