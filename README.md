# 📝 Python To-Do List (MVC Pattern)

A simple **console-based To-Do List** application built using the **Model-View-Controller (MVC)** pattern in Python.

---

## 📁 Project Structure
```
todolist_mvc/
├── init.py # Marks folder as a Python package (optional)
├── model.py # Data layer (Model)
├── view.py # User interface layer (View)
├── controller.py # Application logic (Controller)
└── main.py # Entry point to run the app
```

---

## 🚀 Features

- Add tasks
- View tasks
- Delete tasks by number
- Clean MVC structure for easy maintenance and learning
- Console-based, cross-platform (Linux, macOS, Windows)

---

## 🛠 Requirements

- Python 3.x
- No external libraries needed

---

## ▶️ How to Run

### ✅ Recommended (with package-style imports):

1. Create this folder layout:
```
your_project_folder/
└── todolist_mvc/
├── init.py
├── main.py
├── controller.py
├── model.py
└── view.py
```

2. In `controller.py`, use:
```python
from .model import TaskModel
from .view import TaskView

    In main.py, use:

from .controller import TaskController

    Run from the parent folder:

python3 -m todolist_mvc.main

✅ Alternative (direct run inside folder):

    In controller.py, change imports to:

from model import TaskModel
from view import TaskView

    In main.py:

from controller import TaskController

    Run with:

cd todolist_mvc
python3 main.py

📦 Example Output

Menu:
1. Show tasks
2. Add task
3. Delete task
4. Exit
Choose an option: 2
Enter a new task: Buy groceries
Task added.

Menu:
1. Show tasks
2. Add task
3. Delete task
4. Exit
Choose an option: 1

To-Do List:
  1. Buy groceries

🧠 MVC Layer Responsibilities
Layer	Responsibility	File
Model	Manages task data	model.py
View	Displays UI and gathers input	view.py
Controller	Handles logic and updates model/view	controller.py
📂 License

This project is open-source and free to use for personal or educational purposes.


---

Paste this into a file named `README.md` at the root of your project. Let me know if you want the actual code blocks included inline in the same file as well.
