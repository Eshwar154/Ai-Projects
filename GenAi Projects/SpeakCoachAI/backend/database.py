import sqlite3

def init_db():
    conn = sqlite3.connect("trainer.db")
    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS feedback (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        category TEXT,
                        content TEXT,
                        feedback TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(id))""")
    
    conn.commit()
    conn.close()

init_db()
