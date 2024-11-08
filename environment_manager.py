# environment_manager.py
import subprocess
import sys

class EnvironmentManager:
    """Handles the setup and management of the uv environment."""
    
    @staticmethod
    def check_uv_installed():
        try:
            subprocess.run(['uv', '--version'], check=True, stdout=subprocess.PIPE)
            print("'uv' is already installed.")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("'uv' is not found, it needs to be installed.")
            return False
    
    @staticmethod
    def install_uv_with_snap():
        try:
            subprocess.run(['sudo', 'snap', 'install', 'astral-uv', '--classic'], check=True)
            print("'astral-uv' installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install 'astral-uv': {e}")

    @staticmethod
    def initialize_uv():
        try:
            subprocess.run(['uv', 'init'], check=True)
            print("Initialized uv environment.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to initialize uv environment: {e}")
            sys.exit(1)

    @staticmethod
    def add_django():
        try:
            subprocess.run(['uv', 'add', 'django'], check=True)
            print("Django added to the uv environment.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to add Django to uv environment: {e}")
            sys.exit(1)