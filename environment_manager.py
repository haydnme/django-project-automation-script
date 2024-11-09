import subprocess
import sys

class EnvironmentManager:
    """Handles the setup and configuration of the environment, including checking and installing necessary tools."""

    @staticmethod
    def check_and_install_uv():
        """Check if 'uv' is installed, and if not, prompt the user to install it."""
        if not EnvironmentManager.check_uv_installed():
            if EnvironmentManager.prompt_install_uv():
                EnvironmentManager.install_uv_with_snap()
            else:
                print("UV installation skipped.")
                sys.exit(1)

    @staticmethod
    def check_uv_installed():
        """Check if 'uv' is installed."""
        try:
            subprocess.run(['uv', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("'uv' is already installed.")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("'uv' is not installed.")
            return False

    @staticmethod
    def prompt_install_uv():
        """Prompt the user to install 'uv' if it is not installed."""
        response = input("UV is not installed. Would you like to install it? [y/n]: ").strip().lower()
        return response in ['y', 'yes']

    @staticmethod
    def install_uv_with_snap():
        """Install 'uv' using Snap with classic confinement."""
        try:
            subprocess.run(['sudo', 'snap', 'install', 'astral-uv', '--classic'], check=True)
            print("UV installed successfully.")
        except subprocess.CalledProcessError:
            print("Failed to install 'uv'. Please check your Snap setup.")
            sys.exit(1)

    @staticmethod
    def initialize_uv():
        """Initialize UV."""
        try:
            subprocess.run(['uv', 'init'], check=True)
            print("Initialized UV environment.")
        except subprocess.CalledProcessError:
            print("Failed to initialize UV environment.")
            sys.exit(1)

    @staticmethod
    def add_django():
        """Add Django to the environment using UV."""
        try:
            subprocess.run(['uv', 'add', 'django'], check=True)
            print("Django added to the UV environment.")
        except subprocess.CalledProcessError:
            print("Failed to add Django to the UV environment.")
            sys.exit(1)