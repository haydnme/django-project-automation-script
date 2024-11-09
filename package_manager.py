import subprocess
import sys

class PackageManager:
    """Manages package installation and verification for dependencies."""

    @staticmethod
    def check_snapd_installed():
        """Check if 'snapd' is installed by calling 'snap --version'."""
        try:
            subprocess.run(['snap', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("'snapd' is already installed.")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("'snapd' is not installed or not configured properly.")
            return False

    @staticmethod
    def prompt_install_snapd():
        """Prompt the user to install 'snapd'."""
        response = input("Do you want to install 'snapd'? [y/n]: ")
        if response.lower() in ['yes', 'y']:
            PackageManager.install_package_with_apt('snapd')
        else:
            print("Installation of 'snapd' aborted by the user.")
            sys.exit(1)

    @staticmethod
    def install_package_with_apt(package_name):
        """Install a package using apt."""
        try:
            subprocess.run(['sudo', 'apt', 'install', package_name, '-y'], check=True)
            print(f"{package_name} installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Failed to install '{package_name}'. Please check your system's package manager setup.")
            sys.exit(1)
