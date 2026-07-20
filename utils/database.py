import sqlite3

conn = sqlite3.connect("history.db", check_same_thread=False)
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS captions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    style TEXT,
    caption TEXT
)
""")

conn.commit()


# -----------------------------
# Save Caption
# -----------------------------
def save_caption(username, style, caption):

    cursor.execute(
        """
        INSERT INTO captions(username, style, caption)
        VALUES(?,?,?)
        """,
        (username, style, caption)
    )

    conn.commit()


# -----------------------------
# Get User Captions
# -----------------------------
def get_captions(username):

    cursor.execute(
        """
        SELECT style, caption
        FROM captions
        WHERE username=?
        ORDER BY id DESC
        """,
        (username,)
    )

    return cursor.fetchall()


# -----------------------------
# Delete History
# -----------------------------
def delete_history(username):

    cursor.execute(
        """
        DELETE FROM captions
        WHERE username=?
        """,
        (username,)
    )

    conn.commit()