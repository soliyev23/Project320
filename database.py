import sqlite3
from pathlib import Path

db_path = Path(__file__).resolve().parent / "data.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT * FROM calculations;")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
