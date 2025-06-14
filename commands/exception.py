
class TaskTrackerError(Exception):
    def __init__(self, message: str="Task tracker Error!") -> None:
        self.message = message
        super().__init__(self.message)

class ToManyArgumentError(TaskTrackerError):
    def __init__(self, command: str) -> None:
        super().__init__(f"{command}: to many argument.")

class InvalidArgumentError(TaskTrackerError):
    def __init__(self, argument: str) -> None:
        super().__init__(f"{argument} is invalid argument.")

class TaskNotFoundError(TaskTrackerError):
    def __init__(self, id) -> None:
        super().__init__(f'task {id} not found.')
    