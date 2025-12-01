import json
import os

FILE_JSON = "tasks.json"


class TaskManager:
    def __init__(self):
        if not os.path.exists(FILE_JSON):
            with open(FILE_JSON, "w") as f:
                json.dump([], f)

    # TODO: need to refactor argument parser
    def list_task(self):
        data = self._load_data()
        for idx, item in enumerate(data):
            print(f"{idx + 1}. {item['task']} [{item['status']}]")

    def add_task(self, task):
        data = self._load_data()

        data.append({"task": task, "status": "pending"})

        with open(FILE_JSON, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Added: {task}")

    def complete_task(self, index):
        data = self._load_data()
        # check if index is valid
        if 0 <= index < len(data):
            data[index]["status"] = "done"
            print(f"Task {index + 1} marked as done")
        else:
            print("Invalid task number")

        with open(FILE_JSON, "w") as f:
            json.dump(data, f, indent=4)

    def _load_data(self):
        with open(FILE_JSON, "r") as f:
            return json.load(f)
