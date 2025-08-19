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
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def remind_me_to(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def remind(self):
        # Returns:
        #   A string reminding the user to do the task
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# ---------------------------
#           TASK
# ---------------------------

"""
When given a task title
the task title is save
completed status is false
"""
task = Task("Get Sleep")
        task.title => "Get Sleep"
        task.completed => False

"""
Given an input that is not a string
#rtask raises an exception
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

```



_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
