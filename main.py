import sys
from utils.utils import TaskManager


# TODO: Need better init
def main():
    handler = TaskManager()

    if len(sys.argv) < 2:
        print("Usage:python main.py [add|list] [task_name]")

    command = sys.argv[1]

    if command == "add":
        task_name = "".join(sys.argv[2:])
        handler.add_task(task_name)

    elif command == "list":
        handler.list_task()

    elif command == "help":
        print("Helper method called")
        return

    elif command == "complete":
        index = int(sys.argv[2]) - 1
        handler.complete_task(index)


if __name__ == "__main__":
    main()
