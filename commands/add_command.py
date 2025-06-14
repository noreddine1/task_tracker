from commands.command import Command
from TaskManager import TaskManager

class AddCommand(Command):
    def __init__(self, task_manager: TaskManager) -> None:
        self.task_manager = task_manager
        
    
    def execute(self, args: list[str]):
        if len(args) == 1:
            task = self.task_manager.add_task(args[0].strip())
            print(f'Task added successfully (ID: {task.id})')
            return task
        print("Invalid args. Usage: add <description>")
        return None