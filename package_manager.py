# package_manager.py
import subprocess
import sys

class PackageManager:
    """Handles system package management tasks like checking, installing, and updating packages."""
    
    @staticmethod
    def run_apt_update():
        try:
            subprocess.run(['sudo', 'apt', 'update'], check=True)
            print("Package lists updated successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to update package lists: {e}")
            sys.exit(1)
    
    @staticmethod
    def check_snapd_installed():
        try:
            subprocess.run(['snap', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("'snapd' is already installed.")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("'snapd' is not found, it needs to be installed.")
            return False

    @staticmethod
    def install_package_with_apt(package_name):
        try:
            subprocess.run(['sudo', 'apt', 'install', package_name, '-y'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"{package_name} installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install '{package_name}': {e}")
    
    @staticmethod
    def prompt_install_snapd():
        response = input("Do you want to install 'snapd'? [y/n]: ")
        if response.lower() in ['yes', 'y']:
            PackageManager.install_package_with_apt('snapd')
        else:
            print("Installation of 'snapd' aborted by the user.")
            sys.exit(1)