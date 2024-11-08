# test.py
import os
import shutil
import subprocess
import sys
from directory_manager import DirectoryManager
from package_manager import PackageManager
from environment_manager import EnvironmentManager
from django_project_manager import DjangoProjectManager

def run_tests():
    # Test setup
    test_directory = "app_test"
    test_project_name = "test_project"
    test_app_name = "test_app"
    
    # Ensure starting clean
    if os.path.exists(test_directory):
        shutil.rmtree(test_directory)
    
    # DirectoryManager Test
    print("\n--- DirectoryManager Test ---")
    os.makedirs(test_directory)
    os.chdir(test_directory)
    
    # PackageManager Test
    print("\n--- PackageManager Test ---")
    PackageManager.run_apt_update()
    if not PackageManager.check_snapd_installed():
        PackageManager.prompt_install_snapd()
    
    # EnvironmentManager Test
    print("\n--- EnvironmentManager Test ---")
    if not EnvironmentManager.check_uv_installed():
        EnvironmentManager.install_uv_with_snap()
    EnvironmentManager.initialize_uv()
    EnvironmentManager.add_django()
    
    # DjangoProjectManager Test
    print("\n--- DjangoProjectManager Test ---")
    DjangoProjectManager.create_django_project(test_project_name, test_app_name)
    
    # Verify Directories and Files
    templates_dir = "templates"
    static_dirs = ["static/css", "static/js", "static/img"]
    project_templates_dir = os.path.join(test_project_name, "templates")
    app_templates_dir = os.path.join(test_app_name, "templates", test_app_name)
    
    # Check installation-level templates and static directories
    assert os.path.isdir(templates_dir), "Installation-level templates directory not created."
    for sub_dir in static_dirs:
        assert os.path.isdir(sub_dir), f"Static directory '{sub_dir}' not created."

    # Check project-level template file
    assert os.path.isfile(os.path.join(templates_dir, "base.html")), "base.html not created in templates directory."

    # Check app-level directories and files
    assert os.path.isdir(app_templates_dir), f"App templates directory '{app_templates_dir}' not created."
    assert os.path.isfile(os.path.join(app_templates_dir, "index.html")), "App index.html file not created."
    assert os.path.isfile(f"{test_app_name}/urls.py"), "App urls.py file not created."
    assert os.path.isfile(f"{test_app_name}/forms.py"), "App forms.py file not created."

    # Cleanup
    os.chdir("..")
    shutil.rmtree(test_directory)
    print("\nAll tests completed successfully!")

if __name__ == '__main__':
    run_tests()