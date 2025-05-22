import pytest
from command_parser import extract_command

@pytest.mark.parametrize("input_line,expected_command,expected_rest", [
    ("add task1", "add", "task1"),
    ("delete 123", "delete", "123"),
    ("list", "list", ""),
    ("update 456", "update", "456"),
    ("", "", ""),
    ("add    task1 task2", "add", "task1 task2"),
    ("singleword", "singleword", ""),
    ("   ", "", ""),
])
def test_extract_command(input_line, expected_command, expected_rest):
    command, rest = extract_command(input_line)
    assert command == expected_command
    assert rest == expected_rest