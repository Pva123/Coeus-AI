import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='coeus_user',
        password='secure_password',
        database='CoeusAI'
    )
    return conn

def setup_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Assuming the tables are already created using the provided SQL script
    conn.close()
