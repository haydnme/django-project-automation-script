from setuptools import setup, find_packages

setup(
    name="django-install-configure",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'django-setup=django_setup.main:main'
        ]
    },
    author="Haydn Ellen",
    author_email="haydncoder@gmail.com",
    description="Django project setup tool",
    url="https://haydnellen.com",
)