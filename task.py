import argparse

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

# command handlers (placeholder)

if args.command == "add":
  print("task '" + args.description + "' added") 

if args.command == "list":
    print("current tasks:")
