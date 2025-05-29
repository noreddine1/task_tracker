from Task import Task
class TaskManager:
    def __init__(self):
        self.last_index: int = 0
        self.tasks: list[Task] = []
    
    def add_task(self, description: str, status: str = "todo") -> Task:
        self.last_index += 1
        task = Task(self.last_index, description, status)
        self.tasks.append(task)
        return task
    
    def list_tasks(self, status=None):
        if not status:
            return self.tasks
        return [stask for stask in self.tasks if stask.status == status]