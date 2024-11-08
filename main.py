#!/usr/bin/env python3
import sys
import argparse
from directory_manager import DirectoryManager
from package_manager import PackageManager
from environment_manager import EnvironmentManager
from django_project_manager import DjangoProjectManager

class Application:
    """Main class to orchestrate the setup of the Django project using the above classes."""
    
    @staticmethod
    def run(project_name, app_name):
        """Run the main setup process for creating the Django project and app."""
        if not PackageManager.check_snapd_installed():
            PackageManager.prompt_install_snapd()
        if not EnvironmentManager.check_uv_installed():
            EnvironmentManager.install_uv_with_snap()

        DirectoryManager.prompt_for_directory()
        EnvironmentManager.initialize_uv()
        EnvironmentManager.add_django()
        DjangoProjectManager.create_django_project(project_name, app_name)

def main():
    # Set up argument parser
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
    parser.add_argument('app_name', nargs='?', help="(Optional) Name of the Django app to create within the project")

    # Parse arguments
    args = parser.parse_args()

    # Run the application setup with the provided project and app names
    Application.run(args.project_name, args.app_name)

# Entry point
if __name__ == '__main__':
    main()