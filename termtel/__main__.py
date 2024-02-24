import sys
from subprocess import call
from .generator import generate
import os


# Define ANSI escape codes for text colors
GREEN = '\033[1;32m'
RED = '\033[0;31m'
RESET = '\033[0m'
YELLOW = '\033[1;33m'

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print(f"{RED}Usage: termtel <query>{RESET}")
        sys.exit(1)

    query = sys.argv[1]

    try:
        command = generate(query)
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")
        sys.exit(1)

    choice = input(f"{GREEN}Execute{RESET} {YELLOW}'{command}'{RESET}? (y/N): ")
    if choice.lower() == 'y':
        try:
            os.system(command)
            print(f"{GREEN}Done.{RESET}")
        except Exception as e:
            print(f"{RED}Error executing command: {e}{RESET}")
    else:
        print("Aborted.")

if __name__ == '__main__':
    main()
