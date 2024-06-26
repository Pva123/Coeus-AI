import hashlib
import mysql.connector
from database import get_db_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(username, password, email):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (username, password_hash, email) VALUES (%s, %s, %s)", 
                       (username, hash_password(password), email))
        conn.commit()
        conn.close()
        return True
    except mysql.connector.IntegrityError:
        return False

def login(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM Users WHERE username = %s", (username,))
    result = cursor.fetchone()
    conn.close()
    if result and result[0] == hash_password(password):
        return True
    else:
        return False
