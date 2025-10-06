# config.py
import os

MYSQL_HOST = 'localhost'
MYSQL_USER = 'your_username'
MYSQL_PASSWORD = 'your_password'
MYSQL_DB = 'student'
SECRET_KEY = 'your_flask_secret_key'
LOG_FILE = os.path.join(os.getcwd(), "app.log")
