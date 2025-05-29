from command_parser import parse_command
from icecream import ic
from TaskManager import TaskManager

def execute(taskManager: TaskManager, command: str, argument: str):
    command = command.lower()
    
    match command:
        case "add":
            print(f"Adding task: {argument}")
            taskManager.add_task(argument)
        case "remove":
            print(f"Removing task: {argument}")
        case "list":
            taskManager.list_tasks()
        case "exit":
            print("Exiting....")
            exit(0)
        case _:
            print(f"Unknown command: {command}")

from CLI import CLI

def main():
    taskManager = TaskManager()
    
    cli = CLI(taskManager)
    cli.run()

if __name__ == "__main__":
    main()