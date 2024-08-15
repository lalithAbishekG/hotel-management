import sqlite3

def create_database():
    # Connect to SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rooms (
        room_id INTEGER PRIMARY KEY,
        guest_name TEXT,
        status TEXT
    )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()