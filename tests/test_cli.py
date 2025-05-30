import pytest
from TaskManager import TaskManager
from CLI import CLI

@pytest.fixture
def cli():
    return CLI(TaskManager())

def test_add_task_handler_valid(capsys, cli):
    cli.add_task_handler(["Test task"])
    captured = capsys.readouterr()
    assert 'added successfully' in captured.out.lower()

def test_add_task_handler_invalid(capsys, cli):
    cli.add_task_handler([])
    captured = capsys.readouterr()
    assert 'invalid args' in captured.out.lower()

def test_list_tasks_handler_all(capsys, cli):
    cli.add_task_handler(["Task 1"])
    cli.add_task_handler(["Task 2"])
    cli.list_tasks_handler([])
    captured = capsys.readouterr()
    assert "1: Task 1" in captured.out
    assert "2: Task 2" in captured.out

def test_list_tasks_handler_status(capsys, cli):
    cli.add_task_handler(["Task 1"])
    cli.task_manager.add_task("Task 2", status="done")
    cli.list_tasks_handler(["done"])
    captured = capsys.readouterr()
    assert "Task 2" in captured.out
    assert "Task 1" not in captured.out

def test_list_tasks_handler_invalid_args(capsys, cli):
    cli.list_tasks_handler(["todo", "extra"])
    captured = capsys.readouterr()
    assert "invalid args" in captured.out.lower()

def test_list_tasks_handler_no_tasks(capsys, cli):
    cli.list_tasks_handler([])
    captured = capsys.readouterr()
    assert "no tasks available" in captured.out.lower()

def test_update_task_handler_valid(capsys, cli):
    cli.add_task_handler(["Task 1"])
    cli.update_task_handler(["1", "Updated Task"])
    captured = capsys.readouterr()
    assert 'updated to' in captured.out.lower()
    assert 'updated task' in captured.out.lower()

def test_update_task_handler_invalid_args(capsys, cli):
    cli.update_task_handler(["1"])
    captured = capsys.readouterr()
    assert "invalid args" in captured.out.lower()

def test_update_task_handler_invalid_id(capsys, cli):
    cli.update_task_handler(["abc", "desc"])
    captured = capsys.readouterr()
    assert "invalid id" in captured.out.lower()

def test_update_task_handler_nonexistent_id(capsys, cli):
    cli.update_task_handler(["99", "desc"])
    captured = capsys.readouterr()
    assert "doesn't exist" in captured.out.lower()

def test_delete_task_handler_valid(capsys, cli):
    cli.add_task_handler(["Task 1"])
    cli.delete_task_handler(["1"])
    captured = capsys.readouterr()
    assert "task 1 deleted" in captured.out.lower()

def test_delete_task_handler_invalid_args(capsys, cli):
    cli.delete_task_handler([])
    captured = capsys.readouterr()
    assert "invalid args" in captured.out.lower()

def test_delete_task_handler_invalid_id(capsys, cli):
    cli.delete_task_handler(["abc"])
    captured = capsys.readouterr()
    assert "invalide id" in captured.out.lower() or "invalid id" in captured.out.lower()

def test_delete_task_handler_nonexistent_id(capsys, cli):
    cli.delete_task_handler(["99"])
    captured = capsys.readouterr()
    assert "does not exist" in captured.out.lower() or "could not be deleted" in captured.out.lower()