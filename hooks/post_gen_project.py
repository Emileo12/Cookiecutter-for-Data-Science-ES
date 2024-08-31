
import subprocess


ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"


print(f"{MESSAGE_COLOR}Almost ready!")
print(f"Initializing git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'branch','-m', 'main'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Commit inicial'])

print(f"{MESSAGE_COLOR}The start of your journey begins to shine. Create and have fun!{RESET_ALL}")