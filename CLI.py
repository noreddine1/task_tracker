from icecream import ic
import shlex

from TaskManager import TaskManager

class   CLI:
    def __init__(self, task_manager: TaskManager):
        self.task_manager = task_manager
    
    def run(self):
        while True:
            try:
                user_input = input('task-tacker-cli-> ').strip()
                if not user_input:
                    continue
                parts = shlex.split(user_input)
                command = parts[0].lower()
                match command:
                    case 'add':
                        self.add_task_handler(parts[1:])
                    case 'list':
                        self.list_tasks_handler(parts[1:] if len(parts) > 1 else [])
                    case 'exit':
                        exit(0)
                    case _:
                        print(f'unknown command: {command}')
            except (KeyboardInterrupt, EOFError):
                print('\nUse exit command to exit properly.')


    def add_task_handler(self, args: list[str]):
        if len(args) == 1:
            task = self.task_manager.add_task(args[0])
            print(f'task {task.id} "{task.description}" added succefully.')
        else:
            print("invalid args.")
            task = None
        return task
    