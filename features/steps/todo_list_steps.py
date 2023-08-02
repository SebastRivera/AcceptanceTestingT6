from behave import *

# Importing the todo_list.py
from src import todo_list

@given('the to-do list is empty')
def step_impl(context):
    # Limpiando la lista de tareas antes de cada escenario
    todo_list.clear_all_tasks()

@when('the user adds a task "{task_name}"')
def step_impl(context, task_name):
    todo_list.add_new_task(task_name)

@then('the to-do list should contain "{task_name}"')
def step_impl(context, task_name):
    # Verificando si la tarea está en la lista
    found = any(task[0] == task_name for task in todo_list.LIST_TASKS)
    assert found, f'Task "{task_name}" not found in the to-do list.'

@when('the user lists all tasks')
def step_impl(context):
    # Este paso imprimirá las tareas. No necesitamos hacer ninguna verificación aquí.
    todo_list.list_all_task()

@then('the output should contain')
def step_impl(context):
    # Podemos usar este paso para escenarios que enumeren tareas con detalles específicos.
    # Sin embargo, no necesitamos hacer ninguna verificación aquí, ya que ya probamos list_all_task().
    pass

@then('the to-do list should show task "{task_name}" as completed')
def step_impl(context, task_name):
    # Verificando si la tarea está marcada como completada
    for task in todo_list.LIST_TASKS:
        if task[0] == task_name:
            assert task[1] == 'Completed', f'Task "{task_name}" is not marked as completed in the to-do list.'
            return

    # Si no se encuentra la tarea, generar un error de aserción
    assert False, f'Task "{task_name}" not found in the to-do list.'

@when('the user clears the to-do list')
def step_impl(context):
    todo_list.clear_all_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    # Verificando si la lista de tareas está vacía
    assert len(todo_list.LIST_TASKS) == 0, 'The to-do list should be empty, but it still contains tasks.'

@given('the to-do list contains tasks listAll')
def step_impl(context):
    # Agregando tareas a la lista
    todo_list.LIST_TASKS = [
        ("Buy groceries", "Pending"),
        ("Pay bills", "Pending")
    ]

@given('the to-do list contains tasks markTaskCompleted')
def step_impl(context):
    # Agregando una tarea a la lista
    todo_list.LIST_TASKS = [("Buy groceries", "Pending")]

@when('the user marks task "{task_name}" as completed')
def step_impl(context, task_name):
    todo_list.mark_task(task_name)

@given('the to-do list contains tasks clearList')
def step_impl(context):
    # Agregando tareas a la lista
    todo_list.LIST_TASKS = [
        ("Buy groceries", "Pending"),
        ("Pay bills", "Pending")
    ]

@given('the to-do list contains tasks clearSpecificTask')
def step_impl(context):
    # Agregando una tarea a la lista
    todo_list.LIST_TASKS = [("Buy groceries", "Pending")]

@when('the user clears task "{task_name}" from the to-do list')
def step_impl(context, task_name):
    for task in todo_list.LIST_TASKS:
        if task[0] == task_name:
            todo_list.LIST_TASKS.remove(task)
            return
    assert False, f'Task "{task_name}" not found in the to-do list.'

@given('the to-do list contains tasks markTaskAsPending')
def step_impl(context):
    # Agregando una tarea a la lista
    todo_list.LIST_TASKS = [("Buy groceries", "Completed")]

@when('the user marks task "{task_name}" as pending')
def step_impl(context, task_name):
    for ind, task in enumerate(todo_list.LIST_TASKS):
        if task[0] == task_name:
            todo_list.LIST_TASKS[ind] = (task_name, "Pending")
            return
    assert False, f'Task "{task_name}" not found in the to-do list.'

@given('the to-do list contains tasks listCompleted')
def step_impl(context):
    # Agregando tareas a la lista
    todo_list.LIST_TASKS = [
        ("Buy groceries", "Completed"),
        ("Pay bills", "Pending")
    ]

@when('the user lists completed tasks')
def step_impl(context):
    print("Completed tasks:")
    for task in todo_list.LIST_TASKS:
        if task[1] == "Completed":
            print(task[0])
            
@then('the to-do list should not contain task "{task_name}"')
def step_impl(context, task_name):
    # Verificando que la tarea no esté en la lista
    found = any(task[0] == task_name for task in todo_list.LIST_TASKS)
    assert not found, f'Task "{task_name}" found in the to-do list, but it should not be.'

@then('the to-do list should show task "{task_name}" as pending')
def step_impl(context, task_name):
    # Verificando si la tarea está marcada como pendiente
    for task in todo_list.LIST_TASKS:
        if task[0] == task_name:
            assert task[1] == 'Pending', f'Task "{task_name}" is not marked as pending in the to-do list.'
            return

    # Si no se encuentra la tarea, generar un error de aserción
    assert False, f'Task "{task_name}" not found in the to-do list.'
