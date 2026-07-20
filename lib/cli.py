import argparse
from .models import User,Project,Task
from .storage import save_users,load_users

users = load_users()

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

def main():
    parser = argparse.ArgumentParser(description = "Project Manager")

    subparsers = parser.add_subparsers()

    # add-user
    user_parser = subparsers.add_parser("add-user")
    user_parser.add_argument("--name", required=True)
    user_parser.set_defaults(func=add_user)

    # add-project
    project_parser = subparsers.add_parser("add-project")
    project_parser.add_argument("--user", required=True)
    project_parser.add_argument("--title", required=True)
    project_parser.set_defaults(func=add_project)

    # add-task
    task_parser = subparsers.add_parser("add-task")
    task_parser.add_argument("--user", required=True)
    task_parser.add_argument("--project", required=True)
    task_parser.add_argument("--title", required=True)
    task_parser.set_defaults(func=add_task)

    # view
    view_parser = subparsers.add_parser("view")
    view_parser.set_defaults(func=view_users)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
        save_users(users)


if __name__ == "__main__":
    main()