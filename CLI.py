from icecream import ic
import shlex

from TaskManager import TaskManager
from commands.add_command import AddCommand
from commands.update_command import UpdateCommand
from commands.list_command import ListCommand
from commands.delete_command import DeleteCommand
from commands.mark_commands import MarkInProgressCommand

class CLI:
    def __init__(self, task_manager: TaskManager):
        self.task_manager = task_manager
        self.commands = {
            'add': AddCommand(self.task_manager),
            'update': UpdateCommand(self.task_manager),
            'list': ListCommand(self.task_manager),
            'delete': DeleteCommand(self.task_manager),
            'mark-in-progress': MarkInProgressCommand(self.task_manager)
        }

    def run(self):
        while True:
            try:
                user_input = input('task-tacker-cli-> ').strip()
                if not user_input:
                    continue
                parts = shlex.split(user_input)
                command, *args = parts
                command = command.lower()
                if command == 'exit':
                    exit(0)
                elif command in self.commands:
                    self.commands[command].execute(args)
                else:
                    print(f'Unknown command: `{command}`')
            except (KeyboardInterrupt, EOFError):
                print('\nUse exit command to exit properly.')
            except ValueError as e:
                print(f'Syntax Error: {e}')
            except  Exception as e:
                print(e)


    