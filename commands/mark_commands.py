from .command import Command
from TaskManager import TaskManager
from .exception  import ToManyArgumentError, InvalidArgumentError

class MarkInProgressCommand(Command):
    def __init__(self, task_manager: TaskManager) -> None:
        self.task_manager = task_manager
    
    
    def execute(self, args: list[str]):
        if len(args) > 1:
            raise ToManyArgumentError('mark-in-progress')
        try:
            id = int(args[0])
            self.task_manager.mark_task(id, 'in-progress')
        except ValueError:
            raise InvalidArgumentError(args[0])