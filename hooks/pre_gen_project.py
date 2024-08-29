import os
import sys


project_slug = "{{ cookiecutter.project_slug }}"
python_version = "{{ cookiecutter.python_version }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith("x"):
   print(f"{ERROR_COLOR}ERROR: {project_slug=} no es un nombre valido para el proyecto.\n No empiezes con la letra 'x'.{RESET_ALL}")
   sys.exit(1)


print("Genial! Estas a punto de crear algo increible")
print(f"Creando el proyecto en  {os.getcwd()}")

