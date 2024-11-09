import os
import subprocess
import argparse
from directory_manager import DirectoryManager
from package_manager import PackageManager
from environment_manager import EnvironmentManager
from django_project_manager import DjangoProjectManager

class Application:
    """Main class to orchestrate the setup of the Django project using the above classes."""

    @staticmethod
    def initialize_git(directory):
        """Initialize Git repository in the specified directory if not already initialized."""
        os.chdir(directory)
        if not os.path.exists('.git'):
            subprocess.run(['git', 'init'])
            with open('.gitignore', 'w') as f:
                f.write("*.pyc\n__pycache__/\n.env\n.env-template\nnode_modules/\nstatic/css/output.css\n")
            print("Git repository initialized and .gitignore file created.")
        else:
            print("Git repository already exists in the installation directory.")

    @staticmethod
    def run(project_name, app_name, install_tailwind):
        """Run the main setup process for creating the Django project and app."""
        install_dir = DirectoryManager.prompt_for_directory()
        PackageManager.check_and_install_snapd()

        # Check and initialize UV environment only if not already initialized
        if not os.path.exists(os.path.join(install_dir, 'pyproject.toml')):
            EnvironmentManager.initialize_uv()
        else:
            print("Project is already initialized with UV environment.")

        EnvironmentManager.check_uv_installed()
        Application.initialize_git(install_dir)
        EnvironmentManager.add_django()
        DjangoProjectManager.create_django_project(project_name, app_name)

        if install_tailwind:
            DjangoProjectManager.prompt_tailwind_installation(app_name)
        else:
            print("Skipping Tailwind CSS installation. Only style.css has been created.")

def main():
    parser = argparse.ArgumentParser(description="Setup Django project with optional Tailwind CSS.")
    parser.add_argument('project_name', help="Name of the Django project to create")
    parser.add_argument('app_name', nargs='?', help="(Optional) Name of the Django app to create")
    parser.add_argument('--no-tailwind', action='store_true', help="Skip Tailwind CSS installation")
    args = parser.parse_args()

    Application.run(args.project_name, args.app_name, not args.no_tailwind)

if __name__ == '__main__':
    main()