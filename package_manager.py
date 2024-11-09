import subprocess
import sys

class PackageManager:
    """Handles package management tasks like checking and installing necessary packages."""

    @staticmethod
    def check_and_install_snapd():
        """Check if snapd is installed; if not, prompt the user to install it."""
        if not PackageManager.check_snapd_installed():
            if PackageManager.prompt_install_snapd():
                PackageManager.install_snapd()
            else:
                print("Snapd installation skipped.")
                sys.exit(1)

    @staticmethod
    def check_snapd_installed():
        """Check if 'snapd' is installed."""
        try:
            subprocess.run(['snap', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("'snapd' is already installed.")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("'snapd' is not installed.")
            return False

    @staticmethod
    def prompt_install_snapd():
        """Prompt the user to install 'snapd' if it is not installed."""
        response = input("Snapd is not installed. Would you like to install it? [y/n]: ").strip().lower()
        return response in ['y', 'yes']

    @staticmethod
    def install_snapd():
        """Install 'snapd' using apt."""
        try:
            subprocess.run(['sudo', 'apt', 'install', 'snapd', '-y'], check=True)
            print("Snapd installed successfully.")
        except subprocess.CalledProcessError:
            print("Failed to install 'snapd'. Please check your system's package manager setup.")
            sys.exit(1)

    @staticmethod
    def check_git_installed():
        """Check if 'git' is installed."""
        try:
            subprocess.run(['git', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("'git' is already installed.")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("'git' is not installed.")
            return False

    @staticmethod
    def prompt_install_git():
        """Prompt the user to install 'git' if it is not installed."""
        response = input("Git is not installed. Would you like to install it? [y/n]: ").strip().lower()
        return response in ['y', 'yes']

    @staticmethod
    def install_git():
        """Install 'git' using apt."""
        try:
            subprocess.run(['sudo', 'apt', 'install', 'git', '-y'], check=True)
            print("Git installed successfully.")
        except subprocess.CalledProcessError:
            print("Failed to install 'git'. Please check your system's package manager setup.")
            sys.exit(1)

