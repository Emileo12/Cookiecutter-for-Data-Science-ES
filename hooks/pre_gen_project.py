import os
import sys


project_slug = "{{ cookiecutter.project_slug }}"
python_version = "{{ cookiecutter.python_version }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith("x"):
   print(f"{ERROR_COLOR}ERROR: {project_slug=} is not a valid project name.\n Do not start with the letter 'x'.{RESET_ALL}")
   sys.exit(1)


print("Great! You are about to create something amazing")
print(f"Creating the project in {os.getcwd()}")

