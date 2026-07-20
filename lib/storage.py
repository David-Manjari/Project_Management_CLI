import json
from .models import User, Project, Task

DATA_FILE = "lib/data.json"


def save_users(users):
    data = {}

    for username, user in users.items():
        data[username] = {
            "projects": {}
        }

        for project in user.projects:
            data[username]["projects"][project.title] = {
                "tasks": []
            }

            for task in project.tasks:
                data[username]["projects"][project.title]["tasks"].append({
                    "title": task.title,
                    "completed": task.completed
                })

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_users():
    users = {}

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return users

    for username, user_data in data.items():
        user = User(username)

        for project_title, project_data in user_data["projects"].items():
            project = Project(project_title)

            for task_data in project_data["tasks"]:
                task = Task(task_data["title"])

                if task_data["completed"]:
                    task.completed = True

                project.add_task(task)

            user.add_project(project)

        users[username] = user

    return users