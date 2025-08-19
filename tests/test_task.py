from lib.task import Task
import pytest

def test_task_is_initialised_when_given():
    task = Task("Get Sleep")
    assert task.title == "Get Sleep"
    # task.completed => False

def test_task_complete_status_is_false_by_default():
    task = Task("Get Sleep")
    assert task.completed == False

def test_method_throws_exception_if_title_not_a_string():
    with pytest.raises(Exception) as e:
        task = Task(123)
    assert str(e.value) == "Input needs to be a string!"

def test_method_throws_exception_if_string_is_empty():
    with pytest.raises(Exception) as e:
        task = Task("")
    assert str(e.value) == "Input cannont be empty!"

def test_mark_completed_sets_task_status_to_true():
    task = Task("Buy energy drink")
    task.mark_complete()
    assert task.completed == True

def test_mark_incompleted_sets_task_status_to_False():
    task = Task("Buy energy drink")
    task.mark_complete()
    task.mark_incomplete()
    assert task.completed == False

def test_task_str_changes_with_status():
    task = Task("Buy eneergy drink")
    string_formatted_task = str(task)
    assert "Buy eneergy drink" in string_formatted_task
    assert "✓" not in string_formatted_task


    task.mark_complete()
    string_formatted_task = str(task)
    assert "✓" in string_formatted_task