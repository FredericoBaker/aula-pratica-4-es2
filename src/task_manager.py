class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        if any(t.title == title for t in self.tasks):
            raise ValueError("Já existe uma tarefa com este título.")
        self.tasks.append(Task(title))

    def list_tasks(self):
        return self.tasks

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()
                return
        raise ValueError("Tarefa não encontrada.")

    def remove_task(self, title):
        for i, task in enumerate(self.tasks):
            if task.title == title:
                self.tasks.pop(i)
                return
        raise ValueError("Tarefa não encontrada.")
