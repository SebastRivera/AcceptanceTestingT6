LIST_TASKS = []

def add_new_task(task_name):
    LIST_TASKS.append((task_name, "Pending"))

def list_all_task():
    print("Index - Tasks - Status")
    if len(LIST_TASKS) > 0:
        for ind, task in enumerate(LIST_TASKS):
            print(f"{ind+1} - {task[0]} - {task[1]}")
    else:
        print("There are no tasks to be shown")

def mark_task(task_name):
    list_all_task()
    found = False
    for ind, task in enumerate(LIST_TASKS):
        if task[0] == task_name:
            LIST_TASKS[ind] = (task_name, "Completed")
            found = True
            break

    if not found:
        print(f'Task "{task_name}" not found in the to-do list.')
    else:
        list_all_task()

def clear_all_tasks():
    LIST_TASKS.clear()

def show_options():
    print("Task manager")
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Mark a task as completed")
    print("4. Clear all tasks")
    print("5. Quit")

def main():
    show_options()
    usr_option = input("Enter an option: ")
    usr_option = int(usr_option)
    while usr_option != 5:
        if usr_option == 1:
            task_name = input("Enter the name of the task: ")
            add_new_task(task_name)
        elif usr_option == 2:
            list_all_task()
        elif usr_option == 3:
            task_name = input("Enter the name of the task to mark completed: ")
            mark_task(task_name)
        elif usr_option == 4:
            clear_all_tasks()

        show_options()
        usr_option = input("Enter an option: ")
        usr_option = int(usr_option)

if __name__ == "__main__":
    main()
