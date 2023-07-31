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
                When the user marks task 'Buy groceries' as completed
                Then the to-do list should show task 'Buy groceries' as completed


        @clearList
        Scenario: Clear the entire to-do list
                Given the to-do list contains tasks clearList
                        | Task          |
                        | Buy groceries |
                        | Pay bills     |
                When the user clears the to-do list
                Then the to-do list should be empty


        @addTask
        Scenario: Add multiple tasks to the to-do list
                Given the to-do list is empty addTask
                When the user adds the following tasks:
                        | Buy groceries   |
                        | Pay bills       |
                        | Clean the house |
                Then the to-do list should contain the following tasks:
                        | Task            |
                        | Buy groceries   |
                        | Pay bills       |
                        | Clean the house |


        @removeTask
        Scenario: Remove a task from the to-do list
                Given the to-do list contains tasks removeTask
                        | Task          |
                        | Buy groceries |
                        | Pay bills     |
                When the user removes task 'Buy groceries' from the to-do list
                Then the to-do list should not contain task 'Buy groceries'


        @markTaskPending
        Scenario: Mark a task as pending
                Given the to-do list contains tasks markTaskPending
                        | Task          | Status    |
                        | Buy groceries | Completed |
                When the user marks task 'Buy groceries' as pending
                Then the to-do list should show task 'Buy groceries' as pending