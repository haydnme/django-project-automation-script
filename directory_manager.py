import os
import sys

class DirectoryManager:
    """Handles directory-related operations."""
    
    @staticmethod
    def prompt_for_directory():
        """Prompt user for the installation directory and ensure it is correctly returned."""
        disallowed_names = {'test', 'django', 'site', 'admin', 'main', 'manage', 'static', 'templates', 'media'}
        
        while True:
            directory = input("Enter the installation directory (relative or absolute path) for your Django project: ").strip()
            directory = os.path.abspath(directory)  # Ensure we get an absolute path
            directory_name = os.path.basename(directory)

            if directory_name.lower() in disallowed_names:
                print(f"The directory name '{directory_name}' is reserved. Please choose another name.")
            else:
                try:
                    os.makedirs(directory, exist_ok=True)
                    os.chdir(directory)
                    print(f"Changed directory to {directory}")
                    return directory  # Return the directory path after changing into it
                except Exception as e:
                    print(f"Error creating or accessing the directory: {e}")
