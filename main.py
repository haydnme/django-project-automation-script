#!/usr/bin/env python3
import os
import subprocess
import sys
from directory_manager import DirectoryManager
from package_manager import PackageManager
from environment_manager import EnvironmentManager
from django_project_manager import DjangoProjectManager

class Application:
    """Main class to orchestrate the setup of the Django project using the above classes."""
    
    @staticmethod
    def run(project_name, app_name, install_tailwind=True):
        """Run the main setup process for creating the Django project and app."""
        # Check prerequisites
        if not PackageManager.check_snapd_installed():
            PackageManager.prompt_install_snapd()
        if not EnvironmentManager.check_uv_installed():
            EnvironmentManager.install_uv_with_snap()

        # Create the installation directory and navigate to it
        DirectoryManager.prompt_for_directory()

        # Initialize uv and add Django to the environment
        EnvironmentManager.initialize_uv()
        EnvironmentManager.add_django()

        # Create Django project and app
        DjangoProjectManager.create_django_project(project_name, app_name)

        # Tailwind CSS setup, prompting the user if required
        if install_tailwind:
            DjangoProjectManager.prompt_tailwind_installation(app_name)
        else:
            # Ensure style.css is always created
            os.makedirs("static/css", exist_ok=True)
            with open("static/css/style.css", "w") as f:
                f.write("/* Custom styles */")
            print("Skipping Tailwind CSS installation. Only style.css has been created.")

def main():
    # Set up argument parser
    import argparse
    parser = argparse.ArgumentParser(
        description=(
            "A setup tool to create a Django project with a specified structure, "
            "using the 'uv' environment manager for streamlined package handling."
        ),
        epilog="Author: Haydn Ellen, Ellen Digital, haydncoder@gmail.com, https://haydnellen.com",
        formatter_class=argparse.RawTextHelpFormatter
    )

    # Positional arguments for project name and optional app name
    parser.add_argument('project_name', help="Name of the Django project to create")
    parser.add_argument('app_name', help="Name of the Django app to create within the project")

    # Optional argument for skipping Tailwind installation
    parser.add_argument('--no-tailwind', action='store_true', help="Skip Tailwind CSS installation")

    # Parse arguments
    args = parser.parse_args()

    # Run the application setup with the provided project and app names
    Application.run(args.project_name, args.app_name, not args.no_tailwind)

if __name__ == '__main__':
    main()