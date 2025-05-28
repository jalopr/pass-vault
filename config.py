import os

# Get the base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configuration settings
USER_DB_FILE = os.path.join(os.path.dirname(BASE_DIR), "./users.json")
DATA_FILE = os.path.join(os.path.dirname(BASE_DIR), "./vault.json")

# Function to get configuration
def get_config():
    return {
        "USER_DB_FILE": USER_DB_FILE,
        "DATA_FILE": DATA_FILE
    }