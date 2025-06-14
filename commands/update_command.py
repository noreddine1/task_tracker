from commands.command import Command
from TaskManager import TaskManager

class UpdateCommand(Command):
    def __init__(self, task_manager: TaskManager):
        self.task_manager = task_manager
    
    def execute(self, args: list[str]):
        if len(args) != 2:
            print("Invalid args. Usage: update <id> <new_description>")
            return None
        try:
            id = int(args[0])
        except ValueError:
            print("Invalid id. Id must be an integer.")
            return None
        desc = args[1]
        task = self.task_manager.update_task(id, desc)
        if task:
            print(f'Task {task.id} updated to: "{task.description}"')
        else:
            print(f'task {id} doesn\'t exist.')
        return task   