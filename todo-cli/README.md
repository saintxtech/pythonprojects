# 📝 To-Do List CLI App - Python Project

A simple, file-backed command-line to-do list that lets you manage daily tasks with basic commands.

---

## 🎯 Features

- View, add, and remove tasks
- Saves tasks automatically when you quit
- Loads saved tasks when restarted
- Handles bad input (e.g. non-numeric task removal)

---

## 🧠 Concepts Practiced

- `with open()` → file reading and writing
- `FileNotFoundError` → graceful first-run handling
- `strip()` → remove extra spaces and newlines
- `enumerate()` → show numbered task list
- `append()`, `pop()` → manage a list of tasks
- Basic CLI structure with `if-elif-else` flow

---

## ▶️ How to Run

```bash
python todo.py

Commands:

view → See your tasks

add → Add a new task

remove → Delete a task by number

quit → Save & exit