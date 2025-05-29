import pytest
from TaskManager import TaskManager
from CLI import add_task_handler

def test_add_task_handler_valid(capsys):
    manager = TaskManager()
    add_task_handler(manager, ["Test task"])
    captured = capsys.readouterr()
    assert 'added succefully' in captured.out

def test_add_task_handler_invalid(capsys):
    manager = TaskManager()
    add_task_handler(manager, [])
    captured = capsys.readouterr()
    assert 'invalid args' in captured.out