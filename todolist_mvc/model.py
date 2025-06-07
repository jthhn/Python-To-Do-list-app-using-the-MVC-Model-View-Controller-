# model.py

# This class represent   the data and logic of the application
class TaskModel:
    # Constructor initialize the task list
    def __init__(self):
        self.tasks = []

    # Add task to the list
    def add_task(self, task):
        self.tasks.append(task)

    # Remove a task by its index
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    #Get the current list of tasks
    def get_tasks(self):
        return self.tasks