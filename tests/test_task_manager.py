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

def test_list_tasks_returns_all_tasks_when_no_status():
    manager = TaskManager()
    t1 = manager.add_task('Task 1', 'todo')
    t2 = manager.add_task('Task 2', 'done')
    t3 = manager.add_task('Task 3', 'on-going')
    all_tasks = manager.list_tasks()
    assert all_tasks == [t1, t2, t3]

def test_list_tasks_filters_by_status():
    manager = TaskManager()
    t1 = manager.add_task('Task 1', 'todo')
    t2 = manager.add_task('Task 2', 'done')
    t3 = manager.add_task('Task 3', 'done')
    done_tasks = manager.list_tasks('done')
    assert done_tasks == [t2, t3]
    assert all(task.status == 'done' for task in done_tasks)

def test_list_tasks_returns_empty_when_no_tasks():
    manager = TaskManager()
    assert manager.list_tasks() == []
    assert manager.list_tasks('todo') == []

def test_list_tasks_returns_empty_when_no_status_matches():
    manager = TaskManager()
    manager.add_task('Task 1', 'todo')
    manager.add_task('Task 2', 'on-going')
    assert manager.list_tasks('done') == []

def test_list_tasks_with_multiple_statuses():
    manager = TaskManager()
    t1 = manager.add_task('Task 1', 'todo')
    t2 = manager.add_task('Task 2', 'todo')
    t3 = manager.add_task('Task 3', 'done')
    todo_tasks = manager.list_tasks('todo')
    assert todo_tasks == [t1, t2]
    done_tasks = manager.list_tasks('done')
    assert done_tasks == [t3]

def test_delete_task_removes_task_and_returns_true():
    manager = TaskManager()
    t1 = manager.add_task('Task 1')
    t2 = manager.add_task('Task 2')
    assert manager.delete_task(t1.id) is True
    assert t1 not in manager.tasks
    assert len(manager.tasks) == 1
    assert manager.tasks[0] == t2

def test_delete_task_returns_false_for_invalid_id():
    manager = TaskManager()
    manager.add_task('Task 1')
    result = manager.delete_task(999)  # Non-existent ID
    assert result is False