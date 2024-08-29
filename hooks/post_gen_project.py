
import subprocess


ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"


print(f"{MESSAGE_COLOR}Casi listo!")
print(f"Inicializando repositorio de git...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'branch','-m', 'main'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Commit inicial'])

print(f"{MESSAGE_COLOR}El inicio de tu destino comienza a deslumbrar. Crea y diviertete!{RESET_ALL}")