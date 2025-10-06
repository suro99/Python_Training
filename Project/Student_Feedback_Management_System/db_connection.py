# db_connection.py

import mysql.connector
from mysql.connector import Error
from logger import Logger
from exceptions import DatabaseConnectionError
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DB
            )
            if self.connection.is_connected():
                Logger.write_log("Database connected successfully.")
            return self.connection
        except Error as e:
            Logger.write_log(f"Database connection error: {str(e)}")
            raise DatabaseConnectionError("Failed to connect to database.")

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            Logger.write_log("Database connection closed.")
