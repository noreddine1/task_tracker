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
                        add_task_handler(self.task_manager, parts[1:])
                    case 'exit':
                        exit(0)
                    case _:
                        print(f'unknown command: {command}')
            except (KeyboardInterrupt, EOFError):
                print('\nUse exit command to exit properly.')


def add_task_handler(task_manager: TaskManager, args: list[str]):
    if len(args) == 1:
        task = task_manager.add_task(args[0])
        print(f'task {task.id} "{task.description}" added succefully.')
    else:
        print("invalid args.")
        task = None
    return task
    