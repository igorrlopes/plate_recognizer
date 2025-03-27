import sqlite3

DB_NAME = "plates.db"

def get_all_plates():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authorized_plates")
    plates = cursor.fetchall()
    conn.close()
    return plates

def add_plate(plate):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO authorized_plates (plate) VALUES (?)", (plate.upper(),))
    conn.commit()
    conn.close()

def remove_plate(plate_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM authorized_plates WHERE id = ?", (plate_id,))
    conn.commit()
    conn.close()