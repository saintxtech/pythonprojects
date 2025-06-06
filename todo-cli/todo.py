FILENAME = "tasks.txt"

# Load tasks from file
try:
    with open(FILENAME, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    tasks = []
print("Welcome to Your To Do List App!")
print("Commands: view | add | remove | quit\n")

while True:
    command = input("Enter a command: ").lower()
    if command == "view":
        if not tasks:
            print("Your list is empty.")
        else:
            print("\nTo Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            print()

    elif command == "add":
        new_task = input("Enter a new task: ").strip()
        if new_task:
            tasks.append(new_task)
            print("Task added!")

    elif command == "remove":
        task_num = input("Enter the task number to remove: ")
        if task_num.isdigit():
            index = int(task_num) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        else:
            print("Please enter a number.")
    elif command == "quit":
        # Save tasks to file
        with open(FILENAME, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Tasks saved. Goodbye!")
        break
    else:
        print("Unknown command. Try again.")