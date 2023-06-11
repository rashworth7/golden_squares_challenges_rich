from lib.to_do_list import Tasks
import pytest

"""
Given a task is added to the dict
The dict is updated with the title and description
"""
def test_add_to_list():
    title = "Bins"
    descript = "Take the bins out"
    task_list = Tasks()
    task_list.add(title, descript) # => updates dict to {"Bins": "Take the bins out"}
    to_do_list = task_list.to_do_list

    assert to_do_list == {title: descript}

""" 
Given a task is added which is already in the list
Add raises an exception
"""
def test_add_when_already_added():
    title = "Bins"
    descript = "Take the bins out"
    task_list = Tasks()
    task_list.add("Bins", "Take the bins out") 
    with pytest.raises(Exception) as err:
        task_list.add(title, descript)
    assert str(err.value) == "Task is already on the list!"
    assert task_list.to_do_list == {title: descript}

"""
Given no tasks have been added
returns a statement saying no tasks are on the list
"""
def test_display_no_tasks():
    task_list = Tasks()
    to_do = task_list.display_tasks() # => "No tasks on your to do list!"
    assert to_do == "No tasks on your to do list!"

"""
Given a task has been added
Display that task in the to do dictionary
"""
def test_display_task_for_one_task():
    task_list = Tasks()
    task_list.add("Bins", "Take the bins out")
    to_do_list = task_list.display_tasks() # => {"Bins": "Take the bins out"}
    assert to_do_list == {"Bins": "Take the bins out"}

"""
Given no tasks on the to do list
return an exception when complete task is run
"""
def test_complete_task_when_no_task():
    task_list = Tasks()
    with pytest.raises(Exception) as err:
        task_list.complete_task("Bins")
    assert str(err.value) == "Bins is not on the list, display list to see tasks to complete"

"""
Given two task on the list
return a string telling the user the task is complete
remove the task from the list
"""
def test_complete_task_with_two_tasks():
    title_1, decript_1 = "Bins", "Take the bins out"
    title_2, descript_2 = "Washing", "Hang the washing out on the line"
    task_list = Tasks()
    task_list.add(title_1, decript_1)
    task_list.add(title_2, descript_2)
    message = task_list.complete_task(title_1) # => task_list.to_do_dict = {"Washing": "Hang the washing out"}
    assert task_list.to_do_list == {title_2: descript_2}
    assert message == f"{title_1} completed and removed from the list!"

"""
Given one task on the list and that task is complete
Return a string saying all tasks are complete and update list
"""
def test_complete_task_with_one_task():
    title = "Bins"
    descript = "Take the bins out"
    task_list = Tasks()
    task_list.add(title, descript)
    message = task_list.complete_task(title)
    assert task_list.to_do_list == {}
    assert message == "All tasks completed!"

"""
Given no tasks on the list
update task lets the user know there are no tasks on the list
"""
def test_update_with_task_not_on_list():
    task_list = Tasks()
    with pytest.raises(Exception) as err:
        task_list.update_task("Bins", "Take the bins out")
    assert str(err.value) == "That task is not on the list! Display list to see your outstanding tasks"

"""
Given a task on the list
update task updates the description and returns a string
"""
def test_update_task_already_on_list():
    task_list = Tasks()
    task_list.add("Washing", "Hang the washing out")
    task_list.update_task("Washing", "Bring the washing in") # => task_list.to_do_dict = {}, returns: "task list updated"
    assert task_list.to_do_list == {"Washing": "Bring the washing in"}