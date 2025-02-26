import sqlite3
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT NOT NULL UNIQUE,
               password TEXT NOT NULL
               )
''')
conn.commit()

cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', ('admin', 'admin'))
conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
