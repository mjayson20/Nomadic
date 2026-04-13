"""
Database connection helper.
Reads credentials from environment variables so nothing is hardcoded.

Set these before running:
    DB_HOST     (default: localhost)
    DB_USER     (required)
    DB_PASSWORD (required)
    DB_NAME     (default: nomadic)

On Windows you can put them in a .env file and load with python-dotenv,
or export them in your shell before running main.py.
"""

import os
import mysql.connector as mys
from mysql.connector import Error


def get_connection():
    """Return a new MySQL connection using environment variables."""
    host = os.getenv("DB_HOST", "localhost")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME", "nomadic")

    if not user or not password:
        raise RuntimeError(
            "DB_USER and DB_PASSWORD environment variables must be set."
        )

    return mys.connect(
        host=host,
        user=user,
        passwd=password,
        database=database,
    )


def init_db():
    """
    Create the users table if it does not exist.
    Passwords are stored as bcrypt hashes — never plaintext.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id       INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            role     ENUM('User', 'Nomadic') NOT NULL DEFAULT 'User',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
