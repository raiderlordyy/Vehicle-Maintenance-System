# Vehicle Maintenance & Service Tracking System

Basic SIA1 desktop system built with Python, Tkinter, MySQL, mysql-connector-python, and VS Code.

## Three major components
1. Tkinter GUI
2. Python OOP/application logic
3. MySQL relational database

## Modules
- Login/authentication
- Dashboard
- Vehicle management (CRUD)
- Maintenance records (CRUD)
- Service history

## Setup
1. Install Python 3 and MySQL Server.
2. Open a terminal in this folder and run: `python -m pip install -r requirements.txt`
3. Run `database/schema.sql` in MySQL Workbench or another MySQL client.
4. Set the MySQL credentials in the current PowerShell session with `$env:DB_USER = "your_mysql_username"` and `$env:DB_PASSWORD = "your_mysql_password"`.
5. Run: `python main.py`

Keep these credentials out of source control. The application exits with an error if either variable is missing. Rotate any database password that was previously committed in `config.py`.

## Change Summary

- MySQL credentials are loaded from the `DB_USER` and `DB_PASSWORD` environment variables instead of being stored in `config.py`.
- User passwords use salted PBKDF2-HMAC-SHA256 hashes. Existing plaintext passwords are upgraded to hashes during login.
- The fresh-install administrator password is stored as a hash in the schema. The seeded login remains `admin` / `admin123`; change it after installation.

