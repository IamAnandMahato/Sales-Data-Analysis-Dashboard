import sqlite3
import hashlib

DB_NAME = "users.db"

def create_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username, password):
    create_table()
    conn = create_connection()
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                  (username, hash_password(password)))
        conn.commit()
    except sqlite3.IntegrityError:
        pass

    conn.close()

def login_user(username, password):
    conn = create_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (username, hash_password(password)))

    result = c.fetchone()
    conn.close()

    return result
