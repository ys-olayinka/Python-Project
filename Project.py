import sqlite3

conn = sqlite3.connect('mydatabase1.db')
cursor = conn.cursor()

#create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGer)''')

#insert some data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)",("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)",("Bob", 30))

conn.commit()

#Retrieve data
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
