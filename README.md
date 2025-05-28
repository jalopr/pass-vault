# Pass-Vault v0.2

[![PyPI version](https://img.shields.io/pypi/v/pass-vault.svg)](https://pypi.org/project/pass-vault/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/pass-vault.svg)](https://github.com/yourusername/pass-vault/stargazers)
[![Downloads](https://static.pepy.tech/badge/pass-vault)](https://pepy.tech/project/pass-vault)

A secure command-line password manager built with Python that allows users to safely store, retrieve, and manage their credentials.

## Features

- **Secure User Authentication**: Register and login with bcrypt password hashing
- **Encrypted Password Storage**: All passwords are encrypted using Fernet symmetric encryption
- **Rich CLI Interface**: Colorful and interactive command-line interface using Rich library
- **Password Management**:
  - Add new site credentials
  - Retrieve stored passwords
  - Update existing credentials
  - Delete stored credentials
  - List all stored sites

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/pass-vault.git
   cd pass-vault
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```
python main.py
```

### Main Menu Options

- **Register an Account**: Create a new user account
- **Login to Your Account**: Access your password vault
- **Logout from Session**: End your current session
- **Exit Program**: Close the application

### Password Vault Menu

After logging in, you can:

- **Add Password**: Store credentials for a new site
- **Get Password**: Retrieve credentials for a stored site
- **Update Password**: Modify existing credentials
- **Delete Password**: Remove stored credentials
- **List All Passwords**: View all sites with stored credentials
- **Logout**: Return to the main menu

## Security Features

- Passwords are hashed using bcrypt before storage
- Master password is never stored directly
- Vault data is encrypted using a key derived from your password
- Session management for secure access

## Project Structure

- `main.py`: Entry point of the application
- `menu.py`: Main menu interface
- `menu_vault.py`: Password vault menu interface
- `core.py`: Core authentication and session management
- `vault.py`: Password vault operations
- `config.py`: Configuration settings

## Requirements

- Python 3.6+
- cryptography
- bcrypt
- rich

## License

[MIT License](LICENSE)