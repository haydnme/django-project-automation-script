import subprocess
import sys

class EnvironmentManager:
    """Manages environment setup, including initializing uv and adding Django."""

    @staticmethod
    def check_uv_installed():
        """Check if 'uv' is installed."""
        try:
            subprocess.run(['uv', '--version'], check=True, stdout=subprocess.PIPE)
            print("'uv' is already installed.")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("'uv' is not installed.")
            return False

    @staticmethod
    def install_uv_with_snap():
        """Install 'uv' using Snap with classic confinement."""
        try:
            subprocess.run(['sudo', 'snap', 'install', 'astral-uv', '--classic'], check=True)
            print("'astral-uv' installed successfully.")
        except subprocess.CalledProcessError:
            print("Failed to install 'astral-uv'. Please check your Snap setup.")
            sys.exit(1)

    @staticmethod
    def initialize_uv():
        """Initialize uv environment."""
        try:
            subprocess.run(['uv', 'init'], check=True)
            print("Initialized uv environment.")
        except subprocess.CalledProcessError:
            print("Failed to initialize uv.")
            sys.exit(1)

    @staticmethod
    def add_django():
        """Add Django to the uv environment."""
        try:
            subprocess.run(['uv', 'add', 'django'], check=True)
            print("Django added to the uv environment.")
        except subprocess.CalledProcessError:
            print("Failed to add Django to uv environment.")
            sys.exit(1)