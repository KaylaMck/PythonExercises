todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added.")

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")

def display_tasks():
    print("To-Do List:")
    for task in todo_list:
        print(f"- {task}")

add_task("Read A Book")
add_task("Write Some Code")
add_task("Go for A Walk")

display_tasks()

remove_task("Write Some Code")

display_tasks()