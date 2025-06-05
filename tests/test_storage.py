import pytest
import json
from pathlib import Path
from storage import Storage
from TaskManager import TaskManager

@pytest.fixture
def tmp_data_path(tmp_path):
    return tmp_path / "data.json"

@pytest.fixture
def sample_task_manager():
    tm = TaskManager()
    tm.add_task('task 1')
    tm.add_task('task 2')
    tm.add_task('task 3')
    tm.add_task('task 4')
    return tm

def test_save_creates_file_and_writes_data(tmp_data_path, sample_task_manager):
    storage = Storage(str(tmp_data_path))
    storage.save(sample_task_manager)
    assert tmp_data_path.exists()
    with tmp_data_path.open(encoding='UTF-8') as f:
        data = json.load(f)
    assert data['last_index'] == 4
    # Check that the number of tasks is 4 and each has the expected fields
    assert len(data['tasks']) == 4
    for i, task in enumerate(data['tasks'], 1):
        assert task['id'] == i
        assert task['description'] == f'task {i}'
        assert task['status'] == 'todo'
        assert 'created_at' in task
        assert 'updated_at' in task

from itertools import zip_longest
def test_load_reads_data(tmp_data_path, sample_task_manager):
    # Save data first
    storage = Storage(str(tmp_data_path))
    
    storage.save(sample_task_manager)

    task_manager = TaskManager()
    storage.load(task_manager)
    tasks = list(zip_longest(sample_task_manager.tasks, task_manager.tasks))
    for task1, task2 in zip_longest(sample_task_manager.tasks, task_manager.tasks):
        assert task1.to_dict() == task2.to_dict()
    