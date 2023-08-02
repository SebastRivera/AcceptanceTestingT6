Feature: To-do List

    @addTask
    Scenario: Add a task to the to-do list
        Given the to-do list is empty
        When the user adds a task "Buy groceries"
        Then the to-do list should contain "Buy groceries"

    @listAll
    Scenario: List all tasks in the to-do list.
        Given the to-do list contains tasks listAll
            | Task          |
            | Buy groceries |
            | Pay bills     |
        When the user lists all tasks
        Then the output should contain
            | Tasks         |
            | Buy groceries |
            | Pay bills     |

    @markTaskCompleted
    Scenario:  Mark a task as completed
        Given the to-do list contains tasks markTaskCompleted
            | Task          | Status  |
            | Buy groceries | Pending |
        When the user marks task "Buy groceries" as completed
        Then the to-do list should show task "Buy groceries" as completed

    @clearList
    Scenario: Clear the entire to-do list
        Given the to-do list contains tasks clearList
            | Task          |
            | Buy groceries |
            | Pay bills     |
        When the user clears the to-do list
        Then the to-do list should be empty

    @clearSpecificTask
    Scenario: Clear a specific task from the to-do list
        Given the to-do list contains tasks clearSpecificTask
            | Task          | Status  |
            | Buy groceries | Pending |
        When the user clears task "Buy groceries" from the to-do list
        Then the to-do list should not contain task "Buy groceries"

    @markTaskAsPending
    Scenario: Mark a task as pending (uncompleted)
        Given the to-do list contains tasks markTaskAsPending
            | Task          | Status    |
            | Buy groceries | Completed |
        When the user marks task "Buy groceries" as pending
        Then the to-do list should show task "Buy groceries" as pending

    @listCompleted
    Scenario: List completed tasks
        Given the to-do list contains tasks listCompleted
            | Task          | Status    |
            | Buy groceries | Completed |
            | Pay bills     | Pending   |
        When the user lists completed tasks
        Then the output should contain
            | Tasks         |
            | Buy groceries |