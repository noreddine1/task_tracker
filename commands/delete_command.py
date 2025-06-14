from commands.command import Command
from TaskManager import TaskManager

class DeleteCommand(Command):
    def __init__(self, task_manager: TaskManager):
        self.task_manager = task_manager
    
    def execute(self, args: list[str]):
        if not args:
            print("Invalid args. Usage: delete <id>.")
            return
        try:
            id = int(args[0])
        except ValueError:
            print(f'Invalide id. Id must be integer.')
            return
        if self.task_manager.delete_task(id):
            print(f'task {id} deleted.')
        else:
            print(f'task {id} does not exist or could not be deleted.')