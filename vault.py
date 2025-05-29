import os
import json
import getpass
from config import get_config
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
# Get configuration
config = get_config()
DATA_FILE = config["DATA_FILE"]

# ------------------------------
# --------- FUNCTIONS ----------
# ------------------------------
# Initialize Rich Console
console = Console()
def add_entry(vault, fernet):
    site = Prompt.ask("[bold cyan] Enter Site name[/]").lower()
    if site in vault:
        console.print("[bold red]❌ Site exists, please set different site name.[/]")
        return
    
    username = Prompt.ask("[bold cyan] Enter username[/]")
    password = Prompt.ask("[bold yellow]🔑 Enter password[/]", password=True)
    
    vault[site] = {
        "username": username,
        "password": encrypt(password, fernet)
    }
    save_vault(vault)
    console.print(Panel.fit("[bold green]✔ Password saved.[/]", style="green"))
    
def get_entry(vault, fernet):
    site = Prompt.ask("[bold cyan] Site name to search[/]").lower()
    if site in vault:
        data = vault[site]
        console.print(f"[bold cyan]Username:[/] {data['username']}")
        console.print(f"[bold yellow]Password:[/] {decrypt(data['password'], fernet)}")
        console.print(Panel.fit("[bold blue]GET PASSWORD[/]", style="blue"))
    else:
        console.print("[bold red]❌ Site not found.[/]")

def update_entry(vault, fernet):
    site = Prompt.ask("[bold cyan] Site to update[/]").lower()
    if site in vault:
        username = Prompt.ask("[bold cyan] New username[/]")
        password = Prompt.ask("[bold yellow]🔑 New Password[/]", password=True)
        vault[site] = {
            "username": username,
            "password": encrypt(password, fernet)
        }
        save_vault(vault)
        console.print(Panel.fit("[bold yellow]✔ UPDATE PASSWORD[/]", style="yellow"))
    else:
        console.print("[bold red]❌ Site not found.[/]")

def delete_entry(vault):
    site = Prompt.ask("[bold cyan]Site to delete[/]").lower()
    if site in vault:
        del vault[site]
        save_vault(vault)
        console.print(Panel.fit("[bold red]✔ DELETE PASSWORD[/]", style="red"))
    else:
        console.print("[bold red]❌ Site not found.[/]")

def list_entries(vault):
    if not vault:
        console.print("[bold red]Vault is empty.[/]")
    else:
        console.print("[bold cyan]Stored sites:[/]")
        for site in vault.keys():
            console.print(f" - [green]{site}[/]")
        console.print(Panel.fit("[bold magenta]LIST PASSWORDS[/]", style="magenta"))

def load_vault():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_vault(vault):
    with open(DATA_FILE, "w") as f:
        json.dump(vault, f, indent=4)

def encrypt(text, fernet):
    return fernet.encrypt(text.encode()).decode()

def decrypt(token, fernet):
    return fernet.decrypt(token.encode()).decode()