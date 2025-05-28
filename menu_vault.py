import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.align import Align
from rich.progress import track
from cryptography.fernet import Fernet
from vault import add_entry, load_vault, list_entries
import time
import base64
import hashlib

# Initialize Rich Console
console = Console()

def loading_animation(message, seconds=1):
    for _ in track(range(seconds), description=f"⏳ {message}..."):
        time.sleep(0.3)

def banner():
    from core import banner as main_banner
    main_banner()

def menu_vault(current_user, stored_hash,logout_func):

    """Display password vault operations menu for logged-in users."""
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        banner()
        
        table = Table(title="🔐 PASSWORD VAULT", style="bold cyan", box=None, title_justify="center")
        table.add_column("OPTION", style="bold yellow", justify="center", width=10)
        table.add_column("DESCRIPTION", style="bold white", justify="left", width=30)
        
        table.add_row("1", "ADD PASSWORD")
        table.add_row("2", "GET PASSWORD")
        table.add_row("3", "UPDATE PASSWORD")
        table.add_row("4", "DELETE PASSWORD")
        table.add_row("5", "LIST ALL PASSWORDS")
        table.add_row("0", "LOGOUT")
        
        console.print(Align.center(table))
        console.print(Panel.fit(f"[cyan]Logged in as: {current_user}[/]", style="green"))
        
        choice = Prompt.ask("[bold magenta]👉 SELECT AN OPTION[/]", choices=["1", "2", "3", "4", "5", "0"])
        vault = load_vault()
        # Create a Fernet object from master key
        key = hashlib.sha256(stored_hash.encode()).digest()
        key = hashlib.sha256(key).digest()  # strengthen
        fernet = Fernet(base64.urlsafe_b64encode(key))

        if choice == "1":
            add_entry(vault, fernet)
        elif choice == "2":
            list_entries(vault)
        elif choice == "3":
            update_password()
        elif choice == "4":
            delete_password()
        elif choice == "5":
            list_entries(vault)
        elif choice == "0":
            logout_func()
            return
        
        console.print("\n[bold cyan]Press [Enter] to continue...[/]")
        input()

def add_password():
    console.print(Panel.fit("[bold green]ADD PASSWORD[/]", style="green"))
    # Implementation will go here
    #console.print("[bold cyan]Add Password functionality will be implemented here[/]")
    
def get_password():
    console.print(Panel.fit("[bold blue]GET PASSWORD[/]", style="blue"))
    # Implementation will go here
    console.print("[bold cyan]Get Password functionality will be implemented here[/]")

def update_password():
    console.print(Panel.fit("[bold yellow]UPDATE PASSWORD[/]", style="yellow"))
    # Implementation will go here
    console.print("[bold cyan]Update Password functionality will be implemented here[/]")

def delete_password():
    console.print(Panel.fit("[bold red]DELETE PASSWORD[/]", style="red"))
    # Implementation will go here
    console.print("[bold cyan]Delete Password functionality will be implemented here[/]")

def list_passwords():
    console.print(Panel.fit("[bold magenta]LIST PASSWORDS[/]", style="magenta"))
    # Implementation will go here
    console.print("[bold cyan]List Passwords functionality will be implemented here[/]")