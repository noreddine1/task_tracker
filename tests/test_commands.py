import pytest
from unittest.mock import MagicMock

from commands.add_command import AddCommand
from commands.update_command import UpdateCommand
from commands.list_command import ListCommand
from commands.delete_command import DeleteCommand

@pytest.fixture
def mock_task_manager():
    return MagicMock()

def test_add_command_valid(monkeypatch, mock_task_manager, capsys):
    mock_task = MagicMock(id=42)
    mock_task_manager.add_task.return_value = mock_task
    cmd = AddCommand(mock_task_manager)
    result = cmd.execute(['Test task'])
    captured = capsys.readouterr()
    assert "Task added successfully (ID: 42)" in captured.out
    assert result == mock_task
    mock_task_manager.add_task.assert_called_with('Test task')

def test_add_command_invalid_args(capsys, mock_task_manager):
    cmd = AddCommand(mock_task_manager)
    result = cmd.execute([])
    captured = capsys.readouterr()
    assert "Invalid args. Usage: add <description>" in captured.out
    assert result is None

def test_update_command_valid(monkeypatch, mock_task_manager, capsys):
    mock_task = MagicMock(id=1, description="new desc")
    mock_task_manager.update_task.return_value = mock_task
    cmd = UpdateCommand(mock_task_manager)
    result = cmd.execute(['1', 'new desc'])
    captured = capsys.readouterr()
    assert 'Task 1 updated to: "new desc"' in captured.out
    assert result == mock_task
    mock_task_manager.update_task.assert_called_with(1, 'new desc')

def test_update_command_invalid_args(capsys, mock_task_manager):
    cmd = UpdateCommand(mock_task_manager)
    result = cmd.execute(['1'])
    captured = capsys.readouterr()
    assert "Invalid args. Usage: update <id> <new_description>" in captured.out
    assert result is None

def test_update_command_invalid_id(capsys, mock_task_manager):
    cmd = UpdateCommand(mock_task_manager)
    result = cmd.execute(['abc', 'desc'])
    captured = capsys.readouterr()
    assert "Invalid id. Id must be an integer." in captured.out
    assert result is None

def test_update_command_task_not_found(capsys, mock_task_manager):
    mock_task_manager.update_task.return_value = None
    cmd = UpdateCommand(mock_task_manager)
    result = cmd.execute(['1', 'desc'])
    captured = capsys.readouterr()
    assert "task 1 doesn't exist." in captured.out
    assert result is None

def test_list_command_no_tasks(capsys, mock_task_manager):
    mock_task_manager.list_tasks.return_value = []
    cmd = ListCommand(mock_task_manager)
    result = cmd.execute([])
    captured = capsys.readouterr()
    assert "No tasks available." in captured.out
    assert result is None

def test_list_command_with_tasks(capsys, mock_task_manager):
    mock_task = MagicMock(id=1, description="desc", status="open")
    mock_task_manager.list_tasks.return_value = [mock_task]
    cmd = ListCommand(mock_task_manager)
    result = cmd.execute([])
    captured = capsys.readouterr()
    assert "1: desc [open]" in captured.out
    assert result == [mock_task]

def test_list_command_invalid_args(capsys, mock_task_manager):
    cmd = ListCommand(mock_task_manager)
    result = cmd.execute(['a', 'b'])
    captured = capsys.readouterr()
    assert "Invalid args. Usage: list [status]" in captured.out
    assert result is None

def test_delete_command_valid(capsys, mock_task_manager):
    mock_task_manager.delete_task.return_value = True
    cmd = DeleteCommand(mock_task_manager)
    cmd.execute(['1'])
    captured = capsys.readouterr()
    assert "task 1 deleted." in captured.out
    mock_task_manager.delete_task.assert_called_with(1)

def test_delete_command_invalid_args(capsys, mock_task_manager):
    cmd = DeleteCommand(mock_task_manager)
    cmd.execute([])
    captured = capsys.readouterr()
    assert "Invalid args. Usage: delete <id>." in captured.out
    mock_task_manager.delete_task.assert_not_called()

def test_delete_command_invalid_id(capsys, mock_task_manager):
    cmd = DeleteCommand(mock_task_manager)
    cmd.execute(['abc'])
    captured = capsys.readouterr()
    assert "Invalide id. Id must be integer." in captured.out
    mock_task_manager.delete_task.assert_not_called()

def test_delete_command_not_found(capsys, mock_task_manager):
    mock_task_manager.delete_task.return_value = False
    cmd = DeleteCommand(mock_task_manager)
    cmd.execute(['1'])
    captured = capsys.readouterr()
    assert "task 1 does not exist or could not be deleted." in captured.out

from commands.mark_commands import MarkInProgressCommand
from commands.exception import ToManyArgumentError, InvalidArgumentError

def test_mark_in_progress_valid(mock_task_manager):
    cmd = MarkInProgressCommand(mock_task_manager)
    cmd.execute(['1'])
    mock_task_manager.mark_task.assert_called_with(1, 'in-progress')

def test_mark_in_progress_too_many_args(mock_task_manager):
    cmd = MarkInProgressCommand(mock_task_manager)
    with pytest.raises(ToManyArgumentError):
        cmd.execute(['1', 'extra'])

def test_mark_in_progress_invalid_arg(mock_task_manager):
    cmd = MarkInProgressCommand(mock_task_manager)
    with pytest.raises(InvalidArgumentError):
        cmd.execute(['abc'])

def test_mark_done_valid(mock_task_manager):
    from commands.mark_commands import MarkDone
    cmd = MarkDone(mock_task_manager)
    cmd.execute(['2'])
    mock_task_manager.mark_task.assert_called_with(2, 'done')

def test_mark_done_too_many_args(mock_task_manager):
    from commands.mark_commands import MarkDone
    from commands.exception import ToManyArgumentError
    cmd = MarkDone(mock_task_manager)
    with pytest.raises(ToManyArgumentError):
        cmd.execute(['2', 'extra'])

def test_mark_done_invalid_arg(mock_task_manager):
    from commands.mark_commands import MarkDone
    from commands.exception import InvalidArgumentError
    cmd = MarkDone(mock_task_manager)
    with pytest.raises(InvalidArgumentError):
        cmd.execute(['not-an-int'])