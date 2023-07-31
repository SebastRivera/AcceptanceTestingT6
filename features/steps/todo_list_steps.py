# Importa las funciones necesarias de Behave
from behave import given, when, then

# Lista de tareas que se utilizará para mantener el estado de la to-do list
LIST_TASKS = []

@given('the to-do list is empty')
def step_impl(context):
    # Inicializa la lista de tareas vacía
    LIST_TASKS.clear()

@when('the user adds a task "{task_name}"')
def step_impl(context, task_name):
    # Agrega una nueva tarea con el estado "Pending" a la lista
    LIST_TASKS.append((task_name, "Pending"))

@then('the to-do list should contain "{task_name}"')
def step_impl(context, task_name):
    # Verifica que la tarea esté en la lista
    if (task_name, "Pending") not in LIST_TASKS:
        raise AssertionError(f'Task "{task_name}" not found in the to-do list.')

@when('the user lists all tasks')
def step_impl(context):
    # No es necesario hacer nada aquí, ya que la lista de tareas se imprime en el programa principal
    pass

@then('the output should contain:')
def step_impl(context):
    # Verifica que todas las tareas especificadas en la tabla estén presentes en la lista
    for row in context.table:
        task_name = row['Tasks']
        if (task_name, "Pending") not in LIST_TASKS:
            raise AssertionError(f'Task "{task_name}" not found in the to-do list.')

@given('the to-do list contains tasks markTaskCompleted')
def step_impl(context):
    # Crea la lista de tareas con los estados especificados en la tabla
    for row in context.table:
        task_name = row['Task']
        status = row['Status']
        LIST_TASKS.append((task_name, status))

@when('the user marks task {task_name} as completed')
def step_impl(context, task_name):
    # Marca una tarea como "Completed" en la lista
    for i, (name, status) in enumerate(LIST_TASKS):
        if name == task_name:
            LIST_TASKS[i] = (name, "Completed")
            break
    else:
        raise AssertionError(f'Task "{task_name}" not found in the to-do list.')

@then('the to-do list should show task {task_name} as completed')
def step_impl(context, task_name):
    # Verifica que la tarea esté marcada como "Completed" en la lista
    for name, status in LIST_TASKS:
        if name == task_name:
            if status != "Completed":
                raise AssertionError(f'Task "{task_name}" is not marked as completed in the to-do list.')
            break
    else:
        raise AssertionError(f'Task "{task_name}" not found in the to-do list.')

@given('the to-do list contains tasks clearList')
def step_impl(context):
    # Crea la lista de tareas con los nombres especificados en la tabla
    for row in context.table:
        task_name = row['Task']
        LIST_TASKS.append((task_name, "Pending"))

@when('the user clears the to-do list')
def step_impl(context):
    # Limpia la lista de tareas
    LIST_TASKS.clear()

@then('the to-do list should be empty')
def step_impl(context):
    # Verifica que la lista de tareas esté vacía
    if LIST_TASKS:
        raise AssertionError('The to-do list should be empty, but it still contains tasks.')