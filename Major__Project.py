import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        tasks = [line.strip().split(';') for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f'{task[0]};{task[1]}\n')

def add_task(name, description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append([f'{task_id}', name, description])
    save_tasks(tasks)
    print(f'Task "{name}" added successfully!')

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nTasks List:")
    for task in tasks:
        print(f'{task[0]}. {task[1]}: {task[2]}')

def edit_task(task_id, new_name, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task[0] == str(task_id):
            task[1] = new_name
            task[2] = new_description
            save_tasks(tasks)
            print(f'Task {task_id} edited successfully!')
            return
    print(f'Task with ID {task_id} not found.')

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task[0] != str(task_id)]
    if len(updated_tasks) != len(tasks):
        save_tasks(updated_tasks)
        print(f'Task {task_id} deleted successfully!')
    else:
        print(f'Task with ID {task_id} not found.')

def menu():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a new task")
        print("2. View tasks")
        print("3. Edit a task")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            add_task(name, description)
        
        elif choice == '2':
            view_tasks()
        
        elif choice == '3':
            task_id = input("Enter task ID to edit: ")
            new_name = input("Enter new task name: ")
            new_description = input("Enter new task description: ")
            edit_task(task_id, new_name, new_description)
        
        elif choice == '4':
            task_id = input("Enter task ID to delete: ")
            delete_task(task_id)
        
        elif choice == '5':
            print("Exiting To-Do list application. Goodbye!")
            break
        
        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    menu()
