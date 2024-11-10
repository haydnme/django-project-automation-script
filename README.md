
# Django Project Automation Script

## Summary

This script automates the setup process for Django projects, incorporating additional features such as app creation, Tailwind CSS integration, and Git repository initialization. By managing everything from the project’s directory structure to environment configuration files, it simplifies the Django setup process, allowing developers to focus on development without repetitive setup steps.

## Features

- **Automated Django Project Creation**: Sets up a Django project with an optional app.
- **Structured Directory Creation**: Generates common directories, including `static`, `templates`, and template subdirectories, complete with base HTML files containing Django template blocks.
- **Optional Tailwind CSS Integration**: Prompts for Tailwind CSS setup, creating configuration files (`tailwind.config.js`, `output.css`, `style.css`) as needed.
- **Standalone Git Repository Initialization**: Initializes a Git repository in the project’s installation directory, independent of any parent directories, with a pre-configured `.gitignore` file.
- **Environment File Creation**: Automatically generates `.env` and `.env-template` files with placeholders for configuration values.

## Installation Instructions

** Debian-based systems only.

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/django-project-automation-script.git
   cd django-project-automation-script
   ```

2. **Ensure snapd and uv are installed**: The script will check for snapd and uv (environment manager) and prompt for installation if either is missing.

3. **Run the Script**:
   ```bash
   python main.py <project_name> <app_name> [--no-tailwind]
   ```
   - `<project_name>`: Required. Name of the Django project to create.
   - `<app_name>`: Optional. Name of the Django app to create within the project.
   - `--no-tailwind`: Optional. Use this flag to skip Tailwind CSS setup.

## Usage Instructions

- **Select Installation Directory**: When prompted, specify the installation directory where the Django project and app will be set up.
- **Choose Tailwind CSS Installation**: If Tailwind CSS installation isn’t skipped, the script will prompt for confirmation and set up Tailwind in `static/css`.
- **Verify Git Initialization**: A Git repository will be initialized in the installation directory, with a `.gitignore` to exclude common files, ensuring a standalone Git environment.

## Generated Structure

- HTML template files, with Django template blocks, are created in the `templates` directory.
- `.env` and `.env-template` files with placeholder configurations.
- Static directories and CSS files for Tailwind setup if selected.

## Run the Project

Navigate to your project directory to start the Django server:
   ```bash
   cd <project_name>
   uv run manage.py runserver
   ```

**Author**: Haydn Ellen  
**Website**: [https://haydnellen.com](https://haydnellen.com)
