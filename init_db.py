import sqlite3

def init_db():
    connection = sqlite3.connect('databse.db')
    with open('schema.sql') as f:
        connection.executescript(f.read())
    connection.commit()
    connection.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")

