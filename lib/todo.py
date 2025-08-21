from lib.task import Task


class ToDo():

    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add(self, task):
        if not isinstance(task, Task):
            raise Exception("add method requires a Task instance")
        task.id = self._next_id
        self._next_id += 1
        self.tasks.append(task)
        return task

    def list_completed(self):
        return [str(task) for task in self.tasks if task.completed]

    def list_incomplete(self):
        return [str(task) for task in self.tasks if not task.completed]

    def list_all(self):
        return [str(task) for task in self.tasks]

    def find(self, task_id):
        for task in self.tasks:
            if getattr(task, "id", None) == task_id:
                return task
        return None

    def complete(self, task_id):
        task = self.find(task_id)
        if task is None:
            return False
        task.mark_complete()
        return True

    def remove(self, task_id):
        task = self.find(task_id)
        if task is None:
            return False
        self.tasks.remove(task)
        return True

    def purge_completed(self):
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        return before - len(self.tasks)
