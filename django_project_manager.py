# django_project_manager.py
import os
import subprocess
import sys

class DjangoProjectManager:
    """Manages the creation of Django projects and apps."""
    
    @staticmethod
    def create_django_project(project_name, app_name=None):
        """Create a Django project and optionally an app."""
        try:
            subprocess.run(['uv', 'run', 'django-admin', 'startproject', project_name, '.'], check=True)
            print(f"Django project '{project_name}' created successfully.")
            
            if app_name:
                manage_py_path = 'manage.py'
                subprocess.run(['uv', 'run', 'python', manage_py_path, 'startapp', app_name], check=True)
                print(f"Django app '{app_name}' created successfully.")
                
            DjangoProjectManager.create_additional_folders(app_name)
            DjangoProjectManager.setup_tailwind()
        except subprocess.CalledProcessError as e:
            print(f"Failed to create Django project or app: {str(e)}")
            sys.exit(1)

    @staticmethod
    def create_additional_folders(app_name):
        """Create templates, static folders, initial files, and environment files in the installation directory."""
        # Paths relative to the current working directory (installation directory)
        os.makedirs("templates/partials", exist_ok=True)
        os.makedirs("static/css", exist_ok=True)
        os.makedirs("static/js", exist_ok=True)
        os.makedirs("static/img", exist_ok=True)
        
        # Create the base.html file in the templates directory
        with open("templates/base.html", 'w') as f:
            f.write("<!-- Base HTML Template -->")
        
        # Create a style.css file in the static/css directory
        with open("static/css/style.css", 'w') as f:
            f.write("/* Main stylesheet */")
            print("Created style.css in static/css")

        # App-level directories and files
        if app_name:
            app_template_path = f"{app_name}/templates/{app_name}"
            os.makedirs(app_template_path, exist_ok=True)
            
            # Define the list of HTML files to create
            html_files = {
                "index.html": "<!-- Index HTML Template for app -->",
                "about.html": "<!-- About HTML Template for app -->",
                "contact.html": "<!-- Contact HTML Template for app -->",
                "privacy.html": "<!-- Privacy HTML Template for app -->",
                "portfolio.html": "<!-- Portfolio HTML Template for app -->",
            }
            
            # Create each HTML file with initial content
            for filename, content in html_files.items():
                with open(f"{app_template_path}/{filename}", 'w') as f:
                    f.write(content)
                    print(f"Created {filename} in {app_template_path}")

            # Additional app files
            open(f"{app_name}/urls.py", 'a').close()
            open(f"{app_name}/forms.py", 'a').close()
            print(f"Additional folders and files created in '{app_name}'")
        
        # Create .env and .env-template in the installation directory
        env_content = (
            "# Environment variables\n"
            "DEBUG=True\n"
            "SECRET_KEY=your-secret-key\n"
            "DATABASE_URL=your-database-url\n"
        )
        with open(".env", 'w') as f:
            f.write(env_content)
            print("Created .env in the installation directory.")
        
        with open(".env-template", 'w') as f:
            f.write(env_content)
            print("Created .env-template in the installation directory.")

    @staticmethod
    def check_npm_installed():
        """Check if 'npm' is installed on the system."""
        try:
            subprocess.run(['npm', '--version'], check=True, stdout=subprocess.PIPE)
            print("npm is already installed.")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("npm is not installed.")
            return False

    @staticmethod
    def setup_tailwind():
        """Prompt the user to install Tailwind CSS and set it up if desired."""
        response = input("Do you want to install Tailwind CSS? [y/n]: ").strip().lower()
        if response != 'y':
            print("Skipping Tailwind CSS setup.")
            return
        
        # Check if npm is installed
        if not DjangoProjectManager.check_npm_installed():
            print("Please install npm to proceed with Tailwind CSS setup.")
            sys.exit(1)
        
        # Initialize npm and install Tailwind CSS
        try:
            print("Initializing npm...")
            subprocess.run(['npm', 'init', '-y'], check=True)
            print("Installing Tailwind CSS...")
            subprocess.run(['npm', 'install', 'tailwindcss'], check=True)
            print("Running Tailwind CSS init...")
            subprocess.run(['npx', 'tailwindcss', 'init'], check=True)
            
            # Create tailwind.css in the static/css directory
            tailwind_css_path = "static/css/tailwind.css"
            with open(tailwind_css_path, 'w') as f:
                f.write("/* Tailwind CSS */\n@tailwind base;\n@tailwind components;\n@tailwind utilities;")
            print(f"Created tailwind.css in {tailwind_css_path}")
        
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while setting up Tailwind CSS: {str(e)}")
            sys.exit(1)
