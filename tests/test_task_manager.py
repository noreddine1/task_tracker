import pytest
from TaskManager import TaskManager
from Task import Task

def test_task_manager_initialization():
    manager = TaskManager()
    assert manager.last_index == 0
    assert manager.tasks == []

def test_add_task_increases_last_index_and_appends_task():
    manager = TaskManager()
    task = manager.add_task('Test task')
    assert manager.last_index == 1
    assert len(manager.tasks) == 1
    assert manager.tasks[0] == task
    assert task.description == 'Test task'
    assert isinstance(task, Task)

def test_add_multiple_tasks():
    manager = TaskManager()
    descriptions = ['Task 1', 'Task 2', 'Task 3']
    for i, desc in enumerate(descriptions, 1):
        task = manager.add_task(desc)
        assert task.description == desc
        assert task.id == i
    assert manager.last_index == 3
    assert len(manager.tasks) == 3

def test_add_multiple_tasks_with_status():
    manager = TaskManager()
    descriptions = [('Task 1', 'on-going'), ('Task 2', 'done'), ('Task 3', None)]
    for i, (desc, status) in enumerate(descriptions, 1):
        if status is not None:
            task = manager.add_task(desc, status)
            assert task.status == status
        else:
            task = manager.add_task(desc)
            assert task.status == 'todo'
        assert task.description == desc
        assert task.id == i
    assert manager.last_index == 3
    assert len(manager.tasks) == 3