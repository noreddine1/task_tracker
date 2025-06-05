import json
from TaskManager import TaskManager
from pathlib import Path
from Task import Task

class Storage:
    def __init__(self, path_file: str='data.json'):
        self.path_file = Path(path_file)
    
    def save(self, task_manager: TaskManager) -> bool:
        data = {
            'last_index': task_manager.last_index,
            'tasks': [task.to_dict() for task in task_manager.tasks]
        }
        try:
            with self.path_file.open('w', encoding='UTF-8') as f:
                json.dump(data, f, indent=2)
                return True
        except (IOError, KeyError) as e:
            print(f'Error saving tasks: {e}')
            return False
            
    
    def load(self, task_manager: TaskManager) -> bool:
        if not self.path_file.exists():
            return False
        try:
            with self.path_file.open(encoding='UTF-8') as f:
                data = json.load(f)

            task_manager.last_index = data['last_index']
            task_manager.tasks = [Task.from_dict(task) for task in data.get('tasks')]
            return True
        except json.JSONDecodeError as e:
            print(f'Error invalide json format: {e}')
        except KeyError as e:
            print(f'Missing expected key: {e}')
        except IOError as e:
            print(f'Error file access: {e}')
        return False

