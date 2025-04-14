# A project proposed in "Roadmap.sh"
link: https://roadmap.sh/projects/task-tracker

## App description
Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

## Requirements
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

Add, Update, and Delete tasks
Mark a task as in progress or done
List all tasks
List all tasks that are done
List all tasks that are not done
List all tasks that are in progress
Here are some constraints to guide the implementation:

You can use any programming language to build this project.
Use positional arguments in command line to accept user inputs.
Use a JSON file to store the tasks in the current directory.
The JSON file should be created if it does not exist.
Use the native file system module of your programming language to interact with the JSON file.
Do not use any external libraries or frameworks to build this project.
Ensure to handle errors and edge cases gracefully.

## Example 

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

## Run

Here are some ways to run a demo of the application.

### Docker

A non-persistent demo is available using Docker. Ensure you have Docker installed on your system and that a `Dockerfile` is located in the root of the project.

1.  **Build the Docker image:**
    Navigate to the root directory of the project in your terminal and run the following command to build a Docker image named `task-cli-demo-runner`:
    ```bash
    docker build -t task-cli-demo-runner .
    ```

2.  **Run the Docker container:**
    Once the image has been built, run the container in interactive mode with the following command:
    ```bash
    docker run -it task-cli-demo-runner
    ```

3.  **Use the application:**
    Inside the container, you can interact with the `task-cli` application directly from the terminal. You can use commands like:
    ```bash
    task-cli add "Go to the supermarket"
    task-cli list
    task-cli mark-done 0
    ```
    Refer to the "Examples" section (if it exists) for the specific syntax of the commands.

### Python Interpreter

You can run the application directly using the Python interpreter from the root of the project.

```powershell
python task_cli.py add "Buy bread"
python task_cli.py list todo
```

Or make a wrapper to hide the python interpreter usage like the `cli_wrapper.sh` in the root of the project and run:
``` bash
./cli_wrapper.sh add "Make the bed"
```