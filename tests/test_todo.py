from lib.todo import ToDo
from lib.task import Task

def test_todo_is_initialised_correctly():
    todo = ToDo()
    assert todo.tasks == []
    assert todo._next_id == 1

def test_can_add_task():
    todo = ToDo()
    task = Task("Get Sleep")
    todo.add(task)
    assert todo.tasks == [task]
    assert task.id == 1

# def test_can_list_tasks():
#     todo = ToDo()
#     task1 = Task("Buy milk")
#     task2 = Task("Do laundry")
#     todo.add(task1)
#     todo.add(task2)

#     tasks_list = todo.list_tasks()
#     assert "Buy milk" in tasks_list
#     assert "Do laundry" in tasks_list

from lib.todo import ToDo
from lib.task import Task
import pytest

"""
This is a small test helper class to simulate the Task class.
In a real scenario, you would import the actual Task class.
We are using it here to make this test file self-contained.
"""

def test_todo_initializes_with_empty_list():
    todo = ToDo()
    assert todo.tasks == []
    assert todo._next_id == 1

def test_add_method_adds_task():
    todo = ToDo()
    task = Task("Buy groceries")
    todo.add(task)
    assert len(todo.tasks) == 1
    assert todo.tasks == [task]
    assert todo.tasks[0].id == 1

def test_add_method_raises_error_for_non_task_instance():
    todo = ToDo()
    with pytest.raises(Exception) as e:
        todo.add("This is not a task")
    assert str(e.value) == "add method requires a Task instance"

def test_add_method_increments_id():
    todo = ToDo()
    task1 = Task("Finish Unit 4")
    task2 = Task("Workout")
    todo.add(task1)
    todo.add(task2)
    assert todo.tasks == [task1, task2]
    assert task1.id == 1
    assert task2.id == 2

def test_list_all_returns_all_tasks_as_strings():
    todo = ToDo()
    task1 = Task("Understand TDD")
    task2 = Task("Write tests")
    todo.add(task1)
    todo.add(task2)
    assert todo.list_all() == ["Task 'Understand TDD' [ ]", "Task 'Write tests' [ ]"]

def test_list_completed_returns_only_completed_tasks():
    todo = ToDo()
    task1 = Task("Understand TDD")
    task2 = Task("Write tests")
    todo.add(task1)
    todo.add(task2)
    todo.complete(task2.id)
    assert todo.list_completed() == ["Task 'Write tests' [✓]"]
    assert todo.list_incomplete() == ["Task 'Understand TDD' [ ]"]


def test_find_method_finds_task_by_id():
    todo = ToDo()
    task1 = Task("Task 1")
    task2 = Task("Task 2")
    todo.add(task1)
    todo.add(task2)
    found_task = todo.find(2)
    assert found_task is task2

def test_find_method_returns_none_if_not_found():
    todo = ToDo()
    task_1_id_1 = Task("Task ID = 1")
    todo.add(task_1_id_1)
    found_task = todo.find(2)
    assert found_task is None

def test_complete_method_marks_task_complete():
    todo = ToDo()
    task = Task("Task to complete")
    todo.add(task)
    success = todo.complete(task.id)
    assert success is True
    assert task.completed is True

def test_complete_method_returns_false_if_task_not_found():
    todo = ToDo()
    success = todo.complete(1)
    assert success is False

def test_remove_method_removes_task():
    todo = ToDo()
    task1 = Task("Keep this task")
    task2 = Task("Remove this task")
    todo.add(task1)
    todo.add(task2)
    success = todo.remove(task2.id)
    assert success is True
    assert len(todo.tasks) == 1
    assert task2 not in todo.tasks

def test_remove_method_returns_false_if_task_not_found():
    todo = ToDo()
    success = todo.remove(1)
    assert success is False

def test_purge_completed_removes_completed_tasks():
    todo = ToDo()
    task1 = Task("Task 1")
    task2 = Task("Task 2")
    task3 = Task("Task 3")
    todo.add(task1)
    todo.add(task2)
    todo.add(task3)
    todo.complete(task1.id)
    todo.complete(task3.id)
    
    tasks_removed = todo.purge_completed()
    assert tasks_removed == 2
    assert len(todo.tasks) == 1
    assert todo.tasks[0] is task2