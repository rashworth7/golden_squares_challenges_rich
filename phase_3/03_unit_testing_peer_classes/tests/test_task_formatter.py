from unittest.mock import Mock
from lib.task_formatter import TaskFormatter


"""
test format returns a single task as string when task is completed
"""
def test_format_completed_task():
    task = Mock()
    task.is_complete.return_value = True
    task.title = "Take the bins out"
    

    task_formatter = TaskFormatter(task)
    assert task_formatter.format() == "- [x] Take the bins out"

    
"""
test format returns a single task as string when task is NOT completed
"""
def test_format_uncompleted_task():
    task = Mock()
    task.is_complete.return_value = False
    task.title = "Take the bins out"
    

    task_formatter = TaskFormatter(task)
    assert task_formatter.format() == "- [ ] Take the bins out"
