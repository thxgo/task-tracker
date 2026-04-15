# Task Tracker CLI

A command-line tool to track and manage your tasks from the terminal.

## Requirements 

- Python 3.6+

## Usage

```bash
python3 task.py [arguments]
```

## Commands

| Command | Description |
|---|---| 
| `add ["description"]` | Add a new task |
| `delete [id]` | Delete a task |
| `list [status]`| List tasks, being possible to filter by status |
| `update [id "updated description"]` | Update a task description |
| `mark-done [id]` | Update task status to done |
| `mark-in-progress [id]` | Update task status to in-progress |
