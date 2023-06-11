class Tasks():
# user-facing properties
#   name: string

    def __init__(self):
        self.to_do_list = {}

    def add(self, title, description):
        if title in self.to_do_list:
            raise Exception("Task is already on the list!")
        
        self.to_do_list[title] = description

    def display_tasks(self):
        if self.to_do_list == {}:
            return "No tasks on your to do list!"
        return self.to_do_list

    def complete_task(self, task):
        if task not in self.to_do_list:
            raise Exception(f"{task} is not on the list, display list to see tasks to complete")
       
        del self.to_do_list[task]

        if self.to_do_list == {}:
            return "All tasks completed!"
        
        return f"{task} completed and removed from the list!"

    def update_task(self, task, description):
        if task not in self.to_do_list:
            raise Exception("That task is not on the list! Display list to see your outstanding tasks")
        
        self.to_do_list[task] = description