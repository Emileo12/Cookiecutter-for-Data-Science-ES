import os
import sys
import subprocess


ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"
# Función para crear el ambiente virtual con Conda
def create_conda_env():
    print(f"{MESSAGE_COLOR}Creando ambiente virtual con Conda...{RESET_ALL}")
    env_file = 'environment.yml'
    
    # Verificar si el archivo environment.yml existe
    if not os.path.exists(env_file):
        print(f"{ERROR_COLOR}ERROR: {env_file} no encontrado.{RESET_ALL}")
        sys.exit(1)
    
    # Comando para crear el ambiente con Conda
    command = f'conda env create --file {env_file}'
    
    try:
        subprocess.check_call(command, shell=True)
        print(f"{MESSAGE_COLOR}Ambiente Conda creado con éxito.{RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{ERROR_COLOR}ERROR: Falló la creación del ambiente Conda.{RESET_ALL}")
        sys.exit(1)

# Llama a la función para crear el ambiente Conda
create_conda_env()


print(f"{MESSAGE_COLOR}Casi listo!")
print(f"Inicializando repositorio de git...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Commit inicial'])

print(f"{MESSAGE_COLOR}El inicio de tu destino comienza a deslumbrar. Crea y diviertete!{RESET_ALL}")