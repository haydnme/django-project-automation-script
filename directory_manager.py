import os
import sys

class DirectoryManager:
    """Handles creation and management of directories for the Django project."""

    @staticmethod
    def prompt_for_directory():
        """Prompt user for the directory where the Django project should be installed, ensuring it isn't a reserved name."""
        disallowed_names = {'test', 'django', 'site', 'admin', 'main', 'manage', 'static', 'templates', 'media'}
        while True:
            directory = input("Enter the installation directory (relative or absolute path) for your Django project: ")
            directory = os.path.abspath(directory)
            directory_name = os.path.basename(directory)

            if os.path.exists(directory) and os.listdir(directory):
                print(f"The directory '{directory}' already exists and is not empty. Please choose another location.")
                sys.exit(1)

            if directory_name.lower() in disallowed_names:
                print(f"The directory name '{directory_name}' is reserved and cannot be used. Please choose another name.")
            else:
                os.makedirs(directory, exist_ok=True)
                os.chdir(directory)
                print(f"Changed directory to {directory}")
                break