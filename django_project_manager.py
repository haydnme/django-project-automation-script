import os
import subprocess
import sys

class DjangoProjectManager:
    """Manages the creation of Django projects and apps."""

    @staticmethod
    def create_django_project(project_name, app_name=None):
        """Create a Django project and optionally an app."""
        try:
            # Start Django project
            subprocess.run(['uv', 'run', 'django-admin', 'startproject', project_name, '.'], check=True)
            print(f"Django project '{project_name}' created successfully.")

            # Create Django app if specified
            if app_name:
                manage_py_path = 'manage.py'
                subprocess.run(['uv', 'run', 'python', manage_py_path, 'startapp', app_name], check=True)
                print(f"Django app '{app_name}' created successfully.")

            # Create additional folders and files
            DjangoProjectManager.create_additional_folders(app_name)
        except subprocess.CalledProcessError as e:
            print(f"Failed to create Django project or app: {str(e)}")
            sys.exit(1)

    @staticmethod
    def create_additional_folders(app_name):
        """Create templates, static folders, initial files, and environment files in the installation directory."""
        os.makedirs("templates/partials", exist_ok=True)
        os.makedirs("static/css", exist_ok=True)
        os.makedirs("static/js", exist_ok=True)
        os.makedirs("static/img", exist_ok=True)

        # Create base.html file with boilerplate content
        with open("templates/base.html", 'w') as f:
            f.write("""{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Home{% endblock title %}</title>
    <meta name="description" content="{% block description %}Home Page{% endblock description %}">
    <link rel="stylesheet" href="{% static 'css/output.css' %}">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    {% block content %}{% endblock content %}
</body>
</html>""")
            print("Created base.html in templates directory.")

        # Create HTML files in app's templates directory if app is specified
        if app_name:
            app_template_path = f"{app_name}/templates/{app_name}"
            os.makedirs(app_template_path, exist_ok=True)
            html_files = {
                "index.html": "{% extends 'base.html' %}\n{% block title %}Index{% endblock title %}\n{% block content %}Index Page{% endblock content %}",
                "about.html": "{% extends 'base.html' %}\n{% block title %}About{% endblock title %}\n{% block content %}About Page{% endblock content %}",
                "contact.html": "{% extends 'base.html' %}\n{% block title %}Contact{% endblock title %}\n{% block content %}Contact Page{% endblock content %}",
                "privacy.html": "{% extends 'base.html' %}\n{% block title %}Privacy{% endblock title %}\n{% block content %}Privacy Policy{% endblock content %}",
                "portfolio.html": "{% extends 'base.html' %}\n{% block title %}Portfolio{% endblock title %}\n{% block content %}Portfolio Page{% endblock content %}",
            }

            for filename, content in html_files.items():
                with open(f"{app_template_path}/{filename}", 'w') as f:
                    f.write(content)
                    print(f"Created {filename} in {app_template_path}")

            # Additional app files
            open(f"{app_name}/urls.py", 'w').write("from django.urls import path\n\nurlpatterns = []\n")
            open(f"{app_name}/forms.py", 'w').write("from django import forms\n\n# Define your forms here\n")
            print(f"Additional folders and files created in '{app_name}'")

        # Create .env and .env-template files
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
    def prompt_tailwind_installation(app_name):
        """Prompt to install Tailwind CSS and set it up if confirmed."""
        response = input("Do you want to install Tailwind CSS? [y/n]: ").strip().lower()
        if response == 'y':
            DjangoProjectManager.setup_tailwind(app_name)
        else:
            DjangoProjectManager.create_style_css()
            print("Skipping Tailwind CSS installation. Only style.css has been created.")

    @staticmethod
    def create_style_css():
        """Create a default style.css file in the static/css directory."""
        with open("static/css/style.css", 'w') as f:
            f.write("/* Custom styles */\n")
        print("Created style.css in static/css directory.")

    @staticmethod
    def setup_tailwind(app_name):
        """Set up Tailwind CSS in the Django project."""
        print("Initializing Tailwind CSS...")

        subprocess.run(["npm", "init", "-y"], check=True)
        subprocess.run(["npm", "install", "tailwindcss"], check=True)
        subprocess.run(["npx", "tailwindcss", "init"], check=True)

        # Create tailwind.css for Tailwind input
        with open("static/css/tailwind.css", "w") as f:
            f.write("/* tailwind css */\n@tailwind base;\n@tailwind components;\n@tailwind utilities;\n")

        # Create style.css for custom CSS
        DjangoProjectManager.create_style_css()

        # Update package.json with Tailwind build, watch, and dev scripts
        with open("package.json", "r") as f:
            package_json = f.read()
        package_json = package_json.replace(
            '"scripts": {',
            '"scripts": {\n    "build": "npx tailwindcss -i ./static/css/tailwind.css -o ./static/css/output.css --minify",\n'
            '    "watch": "npx tailwindcss -i ./static/css/tailwind.css -o ./static/css/output.css --watch",\n'
            '    "dev": "npx tailwindcss -i ./static/css/tailwind.css -o ./static/css/output.css --watch",'
        )
        with open("package.json", "w") as f:
            f.write(package_json)

        # Configure tailwind.config.js content paths
        with open("tailwind.config.js", "r") as f:
            config_content = f.read()
        content_paths = [
            '"./templates/**/*.html",',
            '"./static/js/**/*.js",',
            f'"./{app_name}/templates/{app_name}/**/*.html"'
        ]
        config_content = config_content.replace(
            "content: []",
            f"content: [\n    {',\n    '.join(content_paths)}\n]"
        )
        with open("tailwind.config.js", "w") as f:
            f.write(config_content)
        print("Configured Tailwind CSS content paths in tailwind.config.js")

        # Run the build command to create output.css
        subprocess.run(["npm", "run", "build"], check=True)
        print("Tailwind CSS setup complete.")