from icecream import ic
import shlex

from TaskManager import TaskManager

class CLI:
    def __init__(self, task_manager: TaskManager):
        self.task_manager = task_manager

    def run(self):
        while True:
            try:
                user_input = input('task-tacker-cli-> ').strip()
                if not user_input:
                    continue
                parts = shlex.split(user_input)
                command, *args = parts
                command = command.lower()
                match command:
                    case 'add':
                        self.add_task_handler(args)
                    case 'list':
                        self.list_tasks_handler(args)
                    case 'update':
                        self.update_task_handler(args)
                    case 'delete':
                        self.delete_task_handler(args)
                    case 'exit':
                        exit(0)
                    case _:
                        print(f'Unknown command: `{command}`')
            except (KeyboardInterrupt, EOFError):
                print('\nUse exit command to exit properly.')
            except ValueError as e:
                print(f'Syntax Error: {e}')
            except  Exception as e:
                print(e)

    def add_task_handler(self, args: list[str]):
        if len(args) == 1:
            task = self.task_manager.add_task(args[0].strip())
            print(f'Task added successfully (ID: {task.id})')
            return task
        print("Invalid args. Usage: add <description>")
        return None

    def list_tasks_handler(self, args: list[str]):
        """
        Handles the listing of tasks based on provided arguments.
        """
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

    def update_task_handler(self, args: list[str]):
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

    def delete_task_handler(self, args: list[str]):
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
    