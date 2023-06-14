from unittest.mock import Mock
from lib.task_list import TaskList


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour

def test_all_complete_returns_completed():
    #fake.is_complete
    task_list = TaskList()
    fake_complete_task_1 = Mock()
    
    fake_complete_task_1.is_complete.return_value = True
    task_list.add(fake_complete_task_1)

    fake_complete_task_2 = Mock()
    
    fake_complete_task_2.is_complete.return_value = False
    task_list.add(fake_complete_task_2)

    assert task_list.all_complete() == False
