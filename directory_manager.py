# directory_manager.py
import os
import sys

class DirectoryManager:
    """Manages directory operations like checking, creating, and changing directories."""
    
    disallowed_names = {'test', 'django', 'site', 'admin', 'main', 'manage', 'static', 'templates', 'media'}
    
    @staticmethod
    def prompt_for_directory():
        """Prompt user for the installation directory and ensure it's valid."""
        while True:
            directory = input("Enter the installation directory (relative or absolute path) for your Django project: ").strip()
            
            if ' ' in directory:
                print("Error: Directory names cannot contain spaces. Please use hyphens or underscores instead.")
                continue
            
            directory = os.path.abspath(directory)
            directory_name = os.path.basename(directory)

            if os.path.exists(directory) and os.listdir(directory):
                print(f"The directory '{directory}' already exists and is not empty. Please choose another location.")
                sys.exit(1)

            if directory_name.lower() in DirectoryManager.disallowed_names:
                print(f"The directory name '{directory_name}' is reserved and cannot be used. Please choose another name.")
            else:
                try:
                    os.makedirs(directory, exist_ok=True)
                    os.chdir(directory)
                    print(f"Changed directory to {os.getcwd()}")
                except OSError as e:
                    print(f"Failed to create or change into directory '{directory}': {e}")
                    sys.exit(1)
                break