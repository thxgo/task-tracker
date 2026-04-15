import argparse
import json
from datetime import datetime

# parser setup

parser = argparse.ArgumentParser(description="Task Tracker CLI")
subparser = parser.add_subparsers(dest="command")

# subcommand definitions

subparser.add_parser("list")

done_parser = subparser.add_parser("mark-done")
done_parser.add_argument("id")

progress_parser = subparser.add_parser("mark-in-progress")
progress_parser.add_argument("id")

add_parser = subparser.add_parser("add")
add_parser.add_argument("description")

delete_parser = subparser.add_parser("delete")
delete_parser.add_argument("id")

update_parser = subparser.add_parser("update")
update_parser.add_argument("id")
update_parser.add_argument("description")

# parse input

args = parser.parse_args()

# load tasks

try:
    with open("tasks.json", "r") as f:
        content = f.read()
        tasks = json.loads(content)
except FileNotFoundError:
    with open("tasks.json", "w") as f:
        f.write("[]") 
    tasks = []

# set timestamp and generate new task id

now = datetime.now().isoformat()

if len(tasks) == 0:
    new_id = 1
else:
    new_id = max(tasks, key=lambda t: t["id"])["id"] + 1

# command handlers (placeholder)

if args.command == "add":
    new_task = {
            "id": new_id,
            "description": args.description,
            "status": "todo",
            "createdAt": now,
            "updatedAt": now
    }
    tasks.append(new_task)
    with open("tasks.json", "w") as f:
        f.write(json.dumps(tasks))
    print("task '" + args.description + "' added") 

if args.command == "list":
    print("current tasks:\n")
    for t in tasks:
        print(f"{t['id']} - {t['description']} [{t['status']}]")

if args.command == "delete":
    task_id = int(args.id)
    tasks = [task for task in tasks if task["id"] != task_id]
    with open("tasks.json", "w") as f:
        f.write(json.dumps(tasks))
    print("task '" + args.id + "' removed")

if args.command == "update":
    task_id = int(args.id)
    for t in tasks:
        if t["id"] == task_id:
            t["description"] = args.description
            t["updatedAt"] = now
    with open("tasks.json", "w") as f:
        f.write(json.dumps(tasks))
    print("task '" + args.id + "' updated")

if args.command == "mark-done":
    task_id = int (args.id)
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "done"
            t["updatedAt"] = now
    with open("tasks.json", "w") as f:
        f.write(json.dumps(tasks))
    print("task '" + args.id + "' marked done")
if args.command == "mark-in-progress":
    task_id = int (args.id)
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "in-progress"
            t["updatedAt"] = now
    with open("tasks.json", "w") as f:
        f.write(json.dumps(tasks))
    print("task '" + args.id + "' marked in progress")
