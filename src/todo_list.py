
LIST_TASKS = []
def add_new_task():
    task = input("Enter the name of the task: ")
    LIST_TASKS.append((task, "Pending"))
    list_all_task()
def list_all_task():
    print("Index - Tasks - Status")
    if len(LIST_TASKS) > 0:
        for ind, task in enumerate(LIST_TASKS):
            print(f"{ind+1} - {task[0]} - {task[1]}")
    else:
        print("There are no task to be shown")

def mark_task():
    list_all_task()
    if len(LIST_TASKS) > 0:
        usr_option = input("Enter the number of the task to mark completed: ")
        index = int(usr_option) - 1
        LIST_TASKS[index] = (LIST_TASKS[index][0], "Completed")
        list_all_task()
    else:
        print("There are no task to be marked")

def clear_all_tasks():
    LIST_TASKS.clear()
    list_all_task()

def show_options():
    print("Task manager")
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Mark a task as completed")
    print("4. Clear all tasks")
    print("5. Quit")


show_options()
usr_option = input("Enter an option: ")
usr_option = int(usr_option)
while usr_option != 5:
    if usr_option == 1:
        add_new_task()
    elif usr_option == 2:
        list_all_task()
    elif usr_option == 3:
        mark_task()
    elif usr_option == 4:
        clear_all_tasks()

    show_options()
    usr_option = input("Enter an option: ")
    usr_option = int(usr_option)
