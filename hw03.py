import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def print_directory_contents(path, indent=''):
    try:
        if not path.exists():
            print(Fore.RED + f"Шлях не існує: {path}")
            return

        if path.is_dir():
            print(Fore.BLUE + Style.BRIGHT + f"{indent}{path.name}/")
            for item in path.iterdir():
                print_directory_contents(item, indent + '  ')
        else:
            print(Fore.GREEN + f"{indent}{path.name}")
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory_path = Path(sys.argv[1])
        print_directory_contents(directory_path)
    else:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії.")

