import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.align import Align

# Import from core
from core import banner, register, login, logout, status, get_current_user, get_stored_hash

console = Console()

def menu():
    """Display interactive CLI menu without unnecessary reloads."""
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        banner()

        table = Table(title="🔐 SECURE LOGIN SYSTEM", style="bold cyan", box=None, title_justify="center")
        table.add_column("OPTION", style="bold yellow", justify="center", width=10)
        table.add_column("DESCRIPTION", style="bold white", justify="left", width=30)

        table.add_row("1", "REGISTER AN ACCOUNT")
        table.add_row("2", "LOGIN TO YOUR ACCOUNT")
        table.add_row("3", "LOGOUT FROM SESSION")
        table.add_row("4", "SHOW SESSION STATUS")
        table.add_row("0", "EXIT PROGRAM")

        console.print(Align.center(table))
        console.print("\n")

        choice = Prompt.ask("[bold magenta]👉 SELECT AN OPTION[/]", choices=["1", "2", "3", "4", "0"])

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                # Import menu_vault here to avoid circular imports
                user = get_current_user()
                stored_hash = get_stored_hash()
                from menu_vault import menu_vault as vm
                vm(user, stored_hash,logout)
        elif choice == "3":
            logout()
        elif choice == "4":
            status()
        elif choice == "0":
            console.print("[bold red]👋 Exiting... Goodbye![/]")
            break
        
        # ✅ Only pause before returning to menu, avoiding unnecessary clearing
        console.print("\n [bold cyan]Press [Enter] to return to the menu...[/]")
        input()