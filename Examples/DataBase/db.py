import mysql.connector
 
def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        database="product_db",
        user="root",
        password="root"
    )
    return conn