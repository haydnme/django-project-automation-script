# django-project-automation-script

I wanted to learn more about automating system tasks and manipulating directories and folders using Python, and this project seemed ideal for that. 

Runs on Debian-based systems (Debian, Ubuntu, etc).

Create a top-level working directory, pull the repository files, and run python3 main.py --help for instructions.

Basically, if you have a top-level working directory you could use the following command:
python3 main.py project_name app_name
and the script will walk you through the steps to create the project, with supporting directories and files already created for you (e.g. templates directory, base.html file, urls.py and forms.py in the app directory if you specified one, a media directory) for convenience.

The project name is required, the app name is not. If you omit the app name, only a project will be created.

A great little learning project for anyone interested in automation with Python.

