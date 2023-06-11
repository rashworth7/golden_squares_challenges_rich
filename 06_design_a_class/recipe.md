## Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## Class

```python

class Tasks():
    # user-facing properties
    #   name: string

    def __init__(self):
        # Parameters:
        #   None: initalise with an empty dictionary
        # Side effects
        #   Sets the empty dictionary to the self object (instance of that class)

    def add(self, title, description):
        # Paramters:
        #   title: string which is added as a key to dictionary
        #   decription: string which is added as a value to dictionary
        # Returns:
        #   Nothing
        # Side effects:
        #   Saves the new to_do_dict to the self object
        #   Raises an error message if task is already in dict

    def display_tasks(self):
        # Parameters:
        #   None
        # Returns:
        #   to_do_dict
        # Side effects:
        #   returns a string if no tasks are in the dict

    def complete_task(self, task):
        # Parameters:
        #   task: string identifying which task has been done
        # Returns:
        #   string that tells the user the task has been complete
        #   updated to_do_dict
        # Side effects:
        #   updates the to_do_dict
        #   raises an exception if no tasks are in list

    def update_task(self, task):
        # Parameters:
        #   task: string identifying the task to be updated
        # Returns:
        #   Nothing
        # Side effects:
        #   updates the task dict with the new description

```

## Tests

```python

"""
Given a task is added to the dict
The dict is updated with the title and description
"""
task_list = Tasks()
task_list.add("Bins", "Take the bins out") # => updates dict to {"Bins": "Take the bins out"}

"""
Given a task is added which is already in the list
Add raises an exception
""""
task_list = Tasks()
task_list.add("Bins", "Take the bins out") # => updates dict to {"Bins": "Take the bins out"}
task_list.add("Bins", "Take the bins out") # => raises error message "Task is already in list"

"""
Given no tasks have been added
returns a statement saying no tasks are on the list
"""
task_list = Tasks()
task_list.display() # => "No tasks on your to do list!"

"""
Given a task has been added
Display any tasks as a dictionary
"""
task_list = Tasks()
task_list.display() # => {"Bins": "Take the bins out"}

"""
Given no tasks on the to do list
return an exception when complete task is run
"""
task_list = Tasks()
task_list.add("Bins", "Take the bins outs")
task_list.complete_task("Bins") # => "No tasks to complete"

"""
Given two task on the list
return a string telling the user the task is complete
remove the task from the list
"""
task_list = Tasks()
task_list.add("Bins", "Take the bins out")
task_list.add("Washing", "Hang the washing out on the line")
task_list.complete_task("Bins") # => task_list.to_do_dict = {"Washing": "Hang the washing out"}

"""
Given one task on the list and that task is complete
Return a string saying all tasks are complete and update list
"""
task_list = Tasks()
task_list.add("Bins", "Take the bins out")
task_list.complete("Bins") # => task_list.to_do_dict = {}, "All tasks no complete"

"""
Given no tasks on the list
update task lets the user know there are no tasks on the list
"""
task_list = Tasks()
task_list.update("Bins") # => "Bins on your to do list"

"""
Given a task on the list
update task updates the description and returns a string
"""
task_list = Tasks()
task_list.add("Washing", "Hang the washing out")
task_list.update("Washing", "Bring the washing in") # => task_list.to_do_dict = {}, returns: "task list updated"

