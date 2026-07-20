import argparse
from .models import User,Project,Task

users = {}

def add_user(args):
    if args.name in users:
        print("User already exists")
        return
    users[args.name] = User(args.name)
    print(f"User {args.name} added")

def add_project(args):
    user = users.get(args.user)
    if not user:
        print("User not found")
        return
    project = Project(args.title)
    user.add_project(project)

def add_task(args):
    user = users.get(args.user)
    if not user:
        print("User not found")
        return
    project = user.get_project(args.project)

    if not project:
        print("Project not found")
        return
    task = Task(args.title)
    project.add_task(task)
# Code snippet to print the tasks belongint to a user
def view_users(args):
    # access User name
    for name,user in users.items():
        print(f"User: {name}")
        # Acess a list of projects
        for project in user.projetcs:
            print (f"Project {project.title}")
            #Access the tasks belonging to this user
            for task in project.tasks:
                if task.completed:
                    print(f"{task.title} complete")
                else:
                    print(f"{task.title} pending")
