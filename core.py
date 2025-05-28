import os
import json
import bcrypt
import getpass
import time
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich.progress import track
from rich.align import Align
from config import get_config
# Initialize Rich Console
console = Console()
current_user = None  # Global variable for session tracking
masterkey_user = None  # Global variable for session tracking

# ----------- Config -----------
config = get_config()
USER_DB_FILE = config["USER_DB_FILE"]
# ------------------------------

# Function to add smooth loading effect
def loading_animation(message, seconds=1):
    for _ in track(range(seconds), description=f"⏳ {message}..."):
        time.sleep(0.3)

# Load and save users
def load_users():
    if os.path.exists(USER_DB_FILE):
        with open(USER_DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_DB_FILE, "w") as f:
        json.dump(users, f, indent=4)

# Password hashing and verification
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def verify_password(stored_hash, password):
    return bcrypt.checkpw(password.encode(), stored_hash.encode())

# Beautiful Banner
def banner():
    banner_text = Text("""
       ██████╗  █████╗ ███████╗███████╗    ██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗
       ██╔══██╗██╔══██╗██╔════╝██╔════╝    ██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝
    ██████╔╝███████║███████╗███████╗    ██║   ██║███████║██║   ██║██║     ██║   
    ██╔═══╝ ██╔══██║╚════██║╚════██║    ╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║   
    ██║     ██║  ██║███████║███████║     ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║   
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝      ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝    
    """, style="bold magenta", justify="center")

    console.print(Align.center(Panel(banner_text, style="blue", padding=(1, 10))))

# User registration
def register():
    users = load_users()
    console.print(Panel.fit("[cyan]👤 Create a new account[/]", style="green"))
    username = Prompt.ask("[bold cyan] Enter username[/]")

    if username in users:
        console.print("[bold red]⚠ Username already exists![/]")
        return

    password = Prompt.ask("[bold yellow]🔑 Enter new password[/]", password=True)

    if len(password) < 6:
        console.print("[bold red]⚠ Password must be at least 6 characters![/]")
        return
    
    users[username] = hash_password(password)
    save_users(users)
    loading_animation("Registering account", 1)
    console.print("[bold green]✅ Registration successful![/]")

# User login
def login():
    global current_user
    global stored_hash
    users = load_users()
    console.print(Panel.fit("[cyan]🔑 Login to your account[/]", style="blue"))
    username = Prompt.ask("[bold cyan]👤 Enter username[/]")
    password = Prompt.ask("[bold yellow]🔑 Enter password[/]", password=True)

    stored_hash = users.get(username)

    if stored_hash and verify_password(stored_hash, password):
        current_user = username
        loading_animation("Authenticating", 1)
        console.print(Panel.fit(f"[bold green]✅ Welcome, {current_user}! 🎉[/]", style="green"))
        console.print("\n[bold cyan]Press [Enter] to return to continue...[/]")
        input()
        return True
    else:
        console.print(Panel.fit("[bold red]❌ Invalid username or password![/]", style="red"))
        return False

# Logout
def logout():
    global current_user
    if current_user:
        loading_animation("Logging out", 1)
        console.print(Panel.fit(f"[bold blue]👋 {current_user} has logged out.[/]", style="blue"))
        current_user = None
    else:
        console.print("[bold red]⚠ No active session![/]")

# Show session status
def status():
    """Show current login status"""
    if current_user:
        console.print(Panel.fit(f"[bold green]🔹 Logged in as: {current_user}[/]", style="green"))
    else:
        console.print(Panel.fit("[bold red]🔹 No user is logged in.[/]", style="red"))

def get_current_user():
    return current_user

def get_stored_hash():
    return stored_hash