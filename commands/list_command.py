from commands.command import Command
from TaskManager import TaskManager

class ListCommand(Command):
    def __init__(self, task_manager: TaskManager):
        self.task_manager = task_manager
    
    def execute(self, args: list[str]):
        if len(args) > 1:
            print("Invalid args. Usage: list [status]")
            return
        status = args[0] if args else None
        tasks = self.task_manager.list_tasks(status)
        if not tasks:
            print("No tasks available.")
            return
        for task in tasks:
            print(f"{task.id}: {task.description} [{task.status}]")
        return tasks