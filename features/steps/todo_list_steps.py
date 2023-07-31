# Import the behave library
from behave import given, when, then

# Initialize an empty list to hold the to-do tasks
todo_list = []

@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = []


@when('the user adds a task "{task_name}"')
def step_impl(context, task_name):
    context.todo_list.append(task_name)


@then('the to-do list should contain "{task_name}"')
def step_impl(context, task_name):
    if task_name not in context.todo_list:
        raise AssertionError(
            f'Expected to-do list to contain "{task_name}", but it didn\'t.')

# Scenario: List all tasks in the to-do list.


@given('the to-do list contains tasks listAll')
def step_impl(context):
    for row in context.table:
        task_name = row['Task']
        todo_list.append(task_name)


@when('the user lists all tasks')
def step_impl(context):
    return

@then('the output should contain:')
def step_impl(context):
    for row in context.table:
        task_name = row['Tasks']
        if task_name not in todo_list:
            raise AssertionError(
                f'Expected task "{task_name}" not found in the to-do list.')

# Scenario: Mark a task as completed.

@given('the to-do list contains tasks markTaskCompleted')
def step_impl(context):
    for row in context.table:
        task_name = row['Task']
        status = row['Status']
        todo_list[task_name] = status


@when('the user marks task {task_name} as completed')
def step_impl(context, task_name):
    if task_name not in todo_list:
        raise AssertionError(
            f'Task "{task_name}" not found in the to-do list.')
    todo_list[task_name] = 'Completed'


@then('the to-do list should show task {task_name} as completed')
def step_impl(context, task_name):
    if task_name not in todo_list:
        raise AssertionError(
            f'Task "{task_name}" not found in the to-do list.')
    if todo_list[task_name] != 'Completed':
        raise AssertionError(
            f'Task "{task_name}" is not marked as completed in the to-do list.')

# Scenario: Clear the entire to-do list.


@given('the to-do list contains tasks clearList')
def step_impl(context):
    for row in context.table:
        task_name = row['Task']
        todo_list.append(task_name)


@when('the user clears the to-do list')
def step_impl(context):
    todo_list.clear()


@then('the to-do list should be empty')
def step_impl(context):
    if todo_list:
        raise AssertionError(
            'The to-do list should be empty, but it still contains tasks.')

# Scenario: Add multiple tasks to the to-do list


@given('the to-do list is empty addTask')
def step_impl(context):
    context.todo_list = []


@when('the user adds the following tasks:')
def step_impl(context):
    for row in context.table:
        task_name = row['Task']
        context.todo_list.append(task_name)


@then('the to-do list should contain the following tasks:')
def step_impl(context):
    for row in context.table:
        task_name = row['Task']
        if task_name not in context.todo_list:
            raise AssertionError(
                f'Task "{task_name}" not found in the to-do list.')

# Scenario: Remove a task from the to-do list


@given('the to-do list contains tasks removeTask')
def step_impl(context):
    for row in context.table:
        task_name = row['Task']
        todo_list.append(task_name)


@when('the user removes task {task_name} from the to-do list')
def step_impl(context, task_name):
    if task_name not in todo_list:
        raise AssertionError(
            f'Task "{task_name}" not found in the to-do list.')
    todo_list.remove(task_name)


@then('the to-do list should not contain task {task_name}')
def step_impl(context, task_name):
    if task_name in todo_list:
        raise AssertionError(
            f'Task "{task_name}" still found in the to-do list after removal.')

# Scenario: Mark a task as pending


@given('the to-do list contains tasks markTaskPending')
def step_impl(context):
    for row in context.table:
        task_name = row['Task']
        status = row['Status']
        todo_list[task_name] = status


@when('the user marks task {task_name} as pending')
def step_impl(context, task_name):
    if task_name not in todo_list:
        raise AssertionError(
            f'Task "{task_name}" not found in the to-do list.')
    todo_list[task_name] = 'Pending'


@then('the to-do list should show task {task_name} as pending')
def step_impl(context, task_name):
    if task_name not in todo_list:
        raise AssertionError(
            f'Task "{task_name}" not found in the to-do list.')
    if todo_list[task_name] != 'Pending':
        raise AssertionError(
            f'Task "{task_name}" is not marked as pending in the to-do list.')
