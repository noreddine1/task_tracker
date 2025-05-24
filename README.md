<!-- Project from https://roadmap.sh/projects/task-tracker -->
# Task Tracker CLI App

A simple command-line tool to manage your tasks and set their status (to-do, done, on-going).

## Features
- Add new tasks
- Update and delete tasks
- Mark tasks as To-Do, On-Going, or Done
- List all tasks or filter by status

## Status Options
- **To-Do**: Task is yet to be started
- **On-Going**: Task is in progress
- **Done**: Task is completed

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/noreddine1/task_tracker.git
   cd task_tracker
   ```
2. Run the app in your terminal:
   ```bash
   # Example command, replace with your actual run command
   python main.py
   ```

## Command Examples
```
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```

