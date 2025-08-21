class Task():
    def __init__(self, title):
        if type(title) != str:
            raise Exception("Input needs to be a string!")
        elif not title:
            raise Exception("Input cannont be empty!")

        self.title = title
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else ' '
        return f"Task '{self.title}' [{status}]"