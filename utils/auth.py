import sqlite3
import bcrypt


def create_users_table():
    conn = sqlite3.connect("instagram_ai.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password BLOB
    )
    """)

    conn.commit()
    conn.close()


def signup(username, password):
    conn = sqlite3.connect("instagram_ai.db")
    cursor = conn.cursor()

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    try:
        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, hashed)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def login(username, password):
    conn = sqlite3.connect("instagram_ai.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return False

    return bcrypt.checkpw(
        password.encode(),
        row[0]
    )