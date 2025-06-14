from TaskManager import TaskManager
from CLI import CLI
from storage import Storage

def main():
    try:
        task_manager = TaskManager()
        storage = Storage()

        print('loading data...')
        storage.load(task_manager)
        cli = CLI(task_manager)
        cli.run()
    except Exception as e:
        print(f'Error {e}')
    finally:
        print('saving data...')
        storage.save(task_manager)
if __name__ == "__main__":
    main()