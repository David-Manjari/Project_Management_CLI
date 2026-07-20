
class Task:
    def __init__(self,title):
        self.title = title
        self.completed = False
    def complete(self):
        self.completed = True
        print(f"Task {self.title} completed")

class Project:
    def __init__(self,title):
        self.title = title
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)
        print(f"Task {task.title} added to project {self.title}")
    
    def get_task (self,title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None
    
    class User:
        def __init__(self,name):
            self.name = name
            self.projects = []

        def add_project (self,project):
            self.projects.append(project)
            print(f"project {project.title} added to {self.name}")
        
        def get_project(self, title):
            for project in self.projects:
                if project.title == title:
                    return project
            return None