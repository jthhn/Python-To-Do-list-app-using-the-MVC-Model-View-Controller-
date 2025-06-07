# Controller.py
from operator import index

from model import TaskModel
from view import TaskView

# This class manages logic and user flow
class TaskController:
    # initialize with model and view
    def __init__(self):
        self.model = TaskModel()
        self.view = TaskView()

    # Run the app loop
    def run(self):
        while True:
            self.view.show_menu()
            choice = input("Choose an option.")

            if choice == '1':
                tasks = self.model.get_tasks()
                self.view.show_tasks(tasks)

            elif choice == '2':
                task = self.view.get_new_task()
                self.model.add_task(task)
                print("Task added.")

            elif choice == '3':
                tasks = self.model.get_tasks()
                self.view.show_tasks(tasks)
                try:
                    index = self.view.get_task_index()
                    self.model.remove_task(index)
                    print("Task removed.")
                except choice == '4':
                    print('Goodbye!')
                    break
            else:
                print("Invalid option. Try again.")