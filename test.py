import os
import shutil
import subprocess

# Define test variables
PROJECT_NAME = "test_project"
APP_NAME = "test_app"
TEST_DIR = "app_test"
INSTALL_DIR = os.path.join(os.getcwd(), TEST_DIR)
TIMEOUT = 60  # Timeout for each subprocess in seconds

def setup_test_environment():
    """Set up the initial directory structure for testing."""
    os.makedirs(TEST_DIR, exist_ok=True)
    os.chdir(TEST_DIR)
    print(f"Setup test environment at: {INSTALL_DIR}")

def cleanup_test_environment():
    """Remove the test environment directory."""
    os.chdir("..")
    shutil.rmtree(TEST_DIR)

def run_command(command, input_text=None, timeout=TIMEOUT):
    """Run a shell command with automated input."""
    try:
        input_text = f"{INSTALL_DIR}\n" + (input_text or "")  # Automated directory and prompt input
        process = subprocess.Popen(
            command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate(input=input_text.encode(), timeout=timeout)

        print(f"Command '{command}' completed with exit code {process.returncode}")
        print(f"stdout:\n{stdout.decode()}")
        print(f"stderr:\n{stderr.decode()}")

        return process.returncode, stdout.decode(), stderr.decode()
    except subprocess.TimeoutExpired:
        process.kill()
        print(f"Command '{command}' timed out.")
        return 1, "", f"Command '{command}' timed out."

def test_directory_structure():
    """Test the initial creation of the installation directory."""
    print("Testing initial installation directory structure...")
    assert os.path.isdir(INSTALL_DIR), f"Installation directory '{INSTALL_DIR}' not created."

def test_django_project_and_app_creation(with_tailwind=True):
    """Test the creation of a Django project and app, with or without Tailwind CSS."""
    print(f"Testing Django project and app creation (with_tailwind={with_tailwind})...")

    # Run the project setup command, simulating 'y' or 'n' for Tailwind prompt
    tailwind_input = "y\n" if with_tailwind else "n\n"
    tailwind_flag = "" if with_tailwind else "--no-tailwind"
    returncode, stdout, stderr = run_command(f"python3 ../main.py {PROJECT_NAME} {APP_NAME} {tailwind_flag}", tailwind_input)
    assert returncode == 0, f"Project setup failed with error: {stderr}"

    # Verify project and app directories within INSTALL_DIR
    project_path = INSTALL_DIR
    print(f"Checking for project directory at: {project_path}")
    assert os.path.isdir(project_path), f"Project directory '{project_path}' not created."

    app_path = os.path.join(INSTALL_DIR, APP_NAME)
    print(f"Checking for app directory at: {app_path}")
    assert os.path.isdir(app_path), f"App directory '{app_path}' not created."

def test_static_and_templates_directories():
    """Test the creation of static and templates directories within the project directory."""
    print("Testing static and templates directories...")
    static_dirs = ["css", "js", "img"]
    for subdir in static_dirs:
        assert os.path.isdir(f"static/{subdir}"), f"Static subdirectory '{subdir}' not created."
    assert os.path.isdir("templates"), "Main templates directory not created."
    assert os.path.isdir("templates/partials"), "Partials directory not created in templates."
    assert os.path.isfile("templates/base.html"), "base.html not created in templates directory."

def test_app_html_files():
    """Test the creation of HTML files in the app's template directory."""
    print("Testing app HTML files...")
    app_template_dir = f"{APP_NAME}/templates/{APP_NAME}"
    html_files = ["index.html", "about.html", "contact.html", "privacy.html", "portfolio.html"]
    for html_file in html_files:
        assert os.path.isfile(f"{app_template_dir}/{html_file}"), f"{html_file} not created in app template directory."

def test_env_files():
    """Test the creation of .env and .env-template files."""
    print("Testing .env and .env-template files...")
    assert os.path.isfile(".env"), ".env file not created."
    assert os.path.isfile(".env-template"), ".env-template file not created."

def test_urls_and_forms_files():
    """Test the creation of urls.py and forms.py in the app directory."""
    print("Testing urls.py and forms.py files...")
    assert os.path.isfile(f"{APP_NAME}/urls.py"), "urls.py not created in app directory."
    assert os.path.isfile(f"{APP_NAME}/forms.py"), "forms.py not created in app directory."

def test_tailwind_setup():
    """Test the setup of Tailwind CSS and related configuration."""
    print("Testing Tailwind CSS setup...")
    assert os.path.isfile("static/css/tailwind.css"), "tailwind.css file not created in static/css directory."
    assert os.path.isfile("static/css/output.css"), "output.css file not created in static/css directory."
    assert os.path.isfile("static/css/style.css"), "style.css file not created in static/css directory."

def test_no_tailwind_setup():
    """Ensure Tailwind CSS files are not created if Tailwind was not installed."""
    print("Testing no Tailwind CSS setup...")
    assert not os.path.isfile("static/css/tailwind.css"), "tailwind.css file should not be created without Tailwind."
    assert not os.path.isfile("static/css/output.css"), "output.css file should not be created without Tailwind."
    assert os.path.isfile("static/css/style.css"), "style.css file not created in static/css directory."

def run_tests():
    """Run all tests in sequence."""
    setup_test_environment()
    try:
        # Test with Tailwind installation
        test_directory_structure()
        test_django_project_and_app_creation(with_tailwind=True)
        test_static_and_templates_directories()
        test_app_html_files()
        test_env_files()
        test_urls_and_forms_files()
        test_tailwind_setup()

        # Test without Tailwind installation
        cleanup_test_environment()
        setup_test_environment()
        test_django_project_and_app_creation(with_tailwind=False)
        test_static_and_templates_directories()
        test_app_html_files()
        test_env_files()
        test_urls_and_forms_files()
        test_no_tailwind_setup()

        print("\nAll tests passed successfully!")
    except AssertionError as e:
        print(f"Test failed: {e}")
    finally:
        cleanup_test_environment()

if __name__ == "__main__":
    run_tests()