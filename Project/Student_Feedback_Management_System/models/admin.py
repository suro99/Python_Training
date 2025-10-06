# models/admin.py

from db_connection import DatabaseConnection
from exceptions import AuthenticationError
from logger import Logger

class Admin:
    def __init__(self):
        self.db = DatabaseConnection()

    def login(self, username, password):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT admin_id, username, password FROM admins WHERE username = %s",
                (username,)
            )
            record = cursor.fetchone()
            if record and record['password'] == password:
                Logger.write_log(f"Admin login success: {username}")
                return record['admin_id'], record['username']
            else:
                Logger.write_log(f"Admin login failed: {username}")
                raise AuthenticationError("Invalid admin username or password.")
        finally:
            cursor.close()
            self.db.disconnect()

    def view_feedback(self):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT f.feedback_id, f.student_id, s.name as student_name, f.course_id, c.course_name, c.faculty_name, f.rating, f.comments "
                "FROM feedback f "
                "JOIN students s ON f.student_id = s.student_id "
                "JOIN courses c ON f.course_id = c.course_id"
            )
            rows = cursor.fetchall()
            Logger.write_log(f"Admin viewed all feedback. Total records: {len(rows)}")
            return rows
        finally:
            cursor.close()
            self.db.disconnect()
