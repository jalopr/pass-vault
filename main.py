import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Run the main menu
if __name__ == "__main__":
    os.system('chcp 65001')
    from menu import menu
    menu()