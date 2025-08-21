# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Task:
    # User-facing properties:
    #   title: string
    #.  completed: boolean
def __init__(self, title):
     # Parameters:
        #   title: string
        #.  completed: bool
        # Side effects:
        # Completed: set to false
        pass # No code here yet

def mark_complete(self):
    # Parameters: none
    # Side effects:
        # Mark the task as complete (True)
    pass # No code here yet

def mark_incomplete(self):
    # Parameters: none
    # Side effects:
        # Mark the task as incomplete (False)
    pass # No code here yet

def __str__(self):
#dunder method, formatts string so it is readable 
# # status = "✓" if self.completed else ' '
# return:
#   A string showing both the tast and its complete 'status'
    # [Expecting] f"Task '{self.title}' [{status}]"
    pass # No code here yet



class ToDo:

    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
            #creates an empty task_list
            #initialises id for task for task list 
        pass # No code here yet

    def add(self, title):
    # Parameters:
        #   title: String
    #Returns:
        # Confirmeation that string is added
        # Side effects:
        # adds task to task list with todo id
        pass # No code here yet


    def list_completed(self):
        # Parameters:
            #none
        # Returns:
            #A list of compleded taskes
        # Side effects:
        pass # No code here yet
   

    def list_imcomplete(self):
        # Parameters:
            #none
        # Returns:
            #A list of incomplete tasks
        # Side effects:
        pass # No code here yet


    def list_all(self):
    # Parameters:
            #none
        # Returns:
            #A list of all tasks
        # Side effects:
        pass # No code here yet


    def find(self, task_id):
        # Parameters:
            #task_id: String
        # Returns:
            #task object related to task id 
        # Side effects:
        pass # No code here yet



    def complete(self, task_id):
    # Parameters:
            #task_id
        # Returns:
            # True
        # Side effects:
            #Alters task complete status 
        pass # No code here yet


    def remove(self, task_id):
        # Parameters:
            #task_id: String
        # Returns:
            #confirmation of removal
        # Side effects:
        pass # removes task from tasklist

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# ---------------------------
#           TASK
# ---------------------------

"""
When given a task title
the task title is initialised
completed status is false
"""
task = Task("Get Sleep")
        task.title => "Get Sleep"
        task.completed => False

"""
Given an input that is not a string
#task raises an exception
"""
task = Task(123) => Exception("Input needs to be a string!")

"""
Given an input that an empty string
#rtask raises an exception
"""
task = Task("") => Exception("Input cannont be empty!")

"""
when mark complete method is called, it sets the complete status to true 
"""
task = Task("Buy energy drink")
task.mark_complete() => True

"""
when mark incomplete method is called, it sets the complete status to false
"""
task = Task("Buy energy drink")
task.mark_incomplete()
task.mark_complete() => False

""""
Test task string changes in accordance to the completed status
""""

task = Task("Buy energy drink")
string_formatted_task = str(task)
Buy energy drink => in string_formatted_task
[✓] => not in string_formatted_task

task.mark_complete():
string_formatted_task = str(task)
[✓] =>  in string_formatted_task


# ---------------------------
#           TODO
# ---------------------------

"""
When a new ToDo list is initialized
the tasks list is empty
the task ID counter is initialized to 1
"""
    todo = ToDo()
    todo.tasks => []
    todo._next_id => 1


"""
When a valid task is added
it is appended to the tasks list
it is assigned a unique ID thst is incremented 
"""
todo = ToDo()
task1 = Task("Finish Unit 4")
task2 = Task("Workout")
todo.add(task1)
todo.add(task2)
todo.tasks => [task1, task2]
task1.id => 1
task2.id => 2

"""
When a non-Task object is added
it raises a exception
"""
todo.add("non taks obj input") => Exception("add method requires a Task instance")

"""
When there are tasks in the list
it returns a list of all tasks as strings
"""
todo = ToDo()
task1 = Task("Task One")
task2 = Task("Task Two")
todo.add(task1)
todo.add(task2)
todo.list_all() => ["Task 'Task One' [ ]", "Task 'Task Two' [ ]"]

"""
When tasks have different completion statuses
list_completed() returns only the completed tasks as strings
list_incomplete() returns only the incomplete tasks as strings
"""
todo = ToDo()
task1 = Task("Completed Task")
task2 = Task("Incomplete Task")
todo.add(task1)
todo.add(task2)
todo.complete(task1.id)
todo.list_completed() => ["Task 'Completed Task' [✓]"]
todo.list_incomplete() => ["Task 'Incomplete Task' [ ]"]

"""
When a valid ID is provided
it returns the corresponding task object
"""
todo = ToDo()
task = Task("Find task")
todo.add(task)
todo.find(task.id) => task

"""
When an invalid ID is provided
it returns None
"""
todo = ToDo()
todo.find(1) => None

"""
When a valid task ID is provided
the corresponding task is marked as complete
it returns True
"""
todo = ToDo()
task = Task("To Complete")
todo.add(task)
todo.complete(task.id) => True
task.completed => True

"""
When an invalid task ID is provided
it returns False
"""
todo = ToDo()
todo.complete(1) => False


"""

When a valid task ID is provided
the corresponding task is removed from the list
it returns True
"""
todo = ToDo()
task = Task("To Remove")
todo.add(task)
todo.remove(task.id) => True
todo.tasks => []

"""
When an invalid task ID is provided
it returns False
"""
todo = ToDo()
todo.remove(1) => False

"""
When some tasks are completed
it removes all completed tasks from the list
it returns the number of tasks removed
"""
todo = ToDo()
task1 = Task("Completed One")
task2 = Task("Incomplete")
task3 = Task("Completed Two")
todo.add(task1)
todo.add(task2)
todo.add(task3)
todo.complete(task1.id)
todo.complete(task3.id)
todo.purge_completed() => 2
todo.tasks => [task2]

```



_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
