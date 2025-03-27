import sqlite3

conn = sqlite3.connect("plates.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS authorized_plates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plate TEXT UNIQUE NOT NULL
)
""")

plates = ["ABC1234", "XYZ9876", "TEST000"]
cursor.executemany("INSERT OR IGNORE INTO authorized_plates (plate) VALUES (?)", [(p,) for p in plates])

conn.commit()
conn.close()

print("Database initialized.")