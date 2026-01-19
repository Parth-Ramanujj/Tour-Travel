import sqlite3

# Connect to the SQLite database (it will create the file if it does not exist)
conn = sqlite3.connect('example.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Example query to create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER)''')

# Commit changes
conn.commit()

# Example query to insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))

# Commit changes
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Close the connection
conn.close()
