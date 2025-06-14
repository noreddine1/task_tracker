from Task import Task
from commands.exception import TaskNotFoundError
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
    
    def get_task(self, id: int) -> Task | None:
        task_generator = (task for task in self.tasks if task.id == id)
        return  next(task_generator, None)

    def update_task(self, id: int, new_desc: str) -> Task | None:
        task = self.get_task(id)
        if not task:
            return None
        task.description = new_desc
        return task
    
    def delete_task(self, id: int) -> bool:
        task = self.get_task(id)
        if not task:
            return False
        self.tasks.remove(task)
        return True
    
    def mark_task(self, id: int, status: str):
        task = self.get_task(id)
        if not task :
            raise TaskNotFoundError(id)
        task.status = status
        