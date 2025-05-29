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
    
    def list_tasks_handler(self, args: list[str]):
        """
        Handles the listing of tasks based on provided arguments.

        Args:
            args (list[str]): A list of arguments. If empty, lists all tasks.
                If one argument is provided, lists tasks filtered by the argument (e.g., status).

        Returns:
            list: The list of tasks managed by the task manager.

        Side Effects:
            Prints the list of tasks to the console. If no tasks are available or invalid arguments are provided,
            prints an appropriate message.
        """
        if not args:
            tasks = self.task_manager.list_taks()
        elif len(args) == 1:
            tasks = self.task_manager.list_taks(args[0])
        else:
            print("invalid args.")
            return
        if not tasks:
            print("No tasks available.")
            return
        for task in tasks:
            print(f"{task.id}: {task.description} [{task.status}]")
        return self.task_manager.tasks