import argparse
import json

# parser setup

parser = argparse.ArgumentParser(description="Task Tracker CLI")
subparser = parser.add_subparsers(dest="command")

# subcommand definitions

subparser.add_parser("list")
subparser.add_parser("mark-done")
subparser.add_parser("mark-in-progress")

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

# command handlers (placeholder)

if args.command == "add":
    print("task '" + args.description + "' added") 

if args.command == "list":
    print("current tasks:")
