import sys
from handler import TaskHandler


def main():
    handler = TaskHandler()

    if len(sys.argv) < 2:
        print("Usage:python main.py [add|list] [task_name]")
        return

    command = sys.argv[1]

    if command == "add":
        task_name = "".join(sys.argv[2:])
        handler.add_task(task_name)

    elif command == "list":
        handler.list_task()


if __name__ == "__main__":
    main()
