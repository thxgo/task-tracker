import argparse

parser = argparse.ArgumentParser(description="Task Tracker CLI")
subparser = parser.add_subparsers(dest="command")

subparser.add_parser("list")
subparser.add_parser("add")
subparser.add_parser("delete")
subparser.add_parser("mark-done")
subparser.add_parser("mark-in-progress")

args = parser.parse_args()

add_parser = subparser.add_parser("add")

# tasks[] = parser.add_subparsers(dest"task")

if args.command == "add":
    add_parser.add_argument("description")
    print("task" + args.description + "adicionada") # fazer um terceiro subparser? 
if args.command == "list":
    print("as suas tarefas atuais sao:")

# insere aqui o que foi adicionado pelo "add"
