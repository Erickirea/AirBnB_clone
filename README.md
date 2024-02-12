# The AirBnB Clone Project
## Project Overview
Welcome to the initial phase of ALX Airbnb clone project, which is dedicated to shaping the robust backend infrastructure. I seamlessly integrated the backend with a user-friendly console application, employing the powerful cmd module in Python.

##Data Storage
To ensure data persistence and accessibility, I implemented a storage mechanism using the json module in Python. All dynamically generated Python objects are stored in a JSON file, allowing seamless retrieval and manipulation.

##Command Line Interpreter
The command line interpreter (CLI) serves as the frontend of the web application, offering users a Bash-like interface tailored specifically for the Airbnb website's functionalities. The CLI, harmoniously coupled with the backend, enables users to interact with the Airbnb clone seamlessly.

Available Commands
The CLI supports a limited set of commands, each meticulously designed for the Airbnb clone's usage. Some of the key commands include:

* show
* create
* update
* destroy
* count

## Actions Supported

The command line interpreter, in conjunction with the backend and file storage system, supports various actions, including:

* Creating new objects (e.g., User or Place)
* Retrieving objects from storage
* Performing operations on objects (e.g., counting, computing stats)
* Updating attributes of objects
* Destroying objects

## How to use it
The Airbnb Clone Command Line Interface (CLI) provides flexibility by supporting both interactive and non-interactive modes, making it convenient for users to interact with the application.

## Interactive Mode
In interactive mode, the console displays a prompt (hbnb) indicating that users can input and execute commands. After each command execution, the prompt reappears, waiting for the next command.

bash
Copy code
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
## Non-Interactive Mode
In non-interactive mode, the CLI can be run with a command input piped into its execution, allowing immediate execution of the specified command without waiting for user input. No prompt appears in this mode.

bash
Copy code
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
## Format of Command Input
In non-interactive mode, commands can be piped through an echo to execute immediately.
In interactive mode, users type commands at the prompt, and execution occurs upon pressing Enter. The console recognizes commands when the Enter key is pressed.
Exiting the Console
The console can be exited in the following ways:

CTRL + D
CTRL + C
Using the command quit or EOF at the prompt.
Feel free to explore and interact with the Airbnb Clone CLI, providing commands as needed to manage the functionalities of the application. Happy exploring! 🚀
