# view.py

# This class handles displaying information and getting user input
class TaskView:
    # Show all tasks
    def show_tasks(self, tasks):
        print("\nTo-Do List:")
        if not tasks:
            print("  (No tasks Yet")
        else:
            for i, task in enumerate(tasks):
                print(f' {i + 1}. {tasks}')

    # Ask for a new task form the user
    def get_new_task(self):
        return input("Enter a new task:")

    # which task to delete
    def get_task_index(self):
        return int(input("Enter task number to delete: ")) - 1

    # Show a menu of options
    def show_menu(self):
        print("\nMenu:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")