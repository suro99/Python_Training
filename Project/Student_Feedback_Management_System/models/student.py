# models/student.py

from db_connection import DatabaseConnection
from exceptions import DuplicateFeedbackError, AuthenticationError
from logger import Logger

class Student:
    def __init__(self):
        self.db = DatabaseConnection()

    def register(self, name, email, password):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            # check if email exists
            cursor.execute("SELECT student_id FROM students WHERE email = %s", (email,))
            if cursor.fetchone():
                Logger.write_log(f"Registration attempt with duplicate email: {email}")
                raise DuplicateFeedbackError("Email already registered.")
            cursor.execute(
                "INSERT INTO students (name, email, password) VALUES (%s, %s, %s)",
                (name, email, password)
            )
            conn.commit()
            Logger.write_log(f"Student registered: {email}")
        finally:
            cursor.close()
            self.db.disconnect()

    def login(self, email, password):
        conn = self.db.connect()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT student_id, name, password FROM students WHERE email = %s",
                (email,)
            )
            record = cursor.fetchone()
            if record and record['password'] == password:
                Logger.write_log(f"Student login success: {email}")
                return record['student_id'], record['name']
            else:
                Logger.write_log(f"Student login failed: {email}")
                raise AuthenticationError("Invalid email or password.")
        finally:
            cursor.close()
            self.db.disconnect()

    def submit_feedback(self, feedback_entry):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            # check duplicate
            cursor.execute(
                "SELECT feedback_id FROM feedback WHERE student_id = %s AND course_id = %s",
                (feedback_entry.student_id, feedback_entry.course_id)
            )
            if cursor.fetchone():
                Logger.write_log(f"Duplicate feedback attempt: student {feedback_entry.student_id}, course {feedback_entry.course_id}")
                raise DuplicateFeedbackError("Feedback already submitted for this course.")
            cursor.execute(
                "INSERT INTO feedback (student_id, course_id, rating, comments) VALUES (%s, %s, %s, %s)",
                (feedback_entry.student_id, feedback_entry.course_id, feedback_entry.rating, feedback_entry.comments)
            )
            conn.commit()
            Logger.write_log(f"Feedback submitted by student {feedback_entry.student_id} for course {feedback_entry.course_id}")
        finally:
            cursor.close()
            self.db.disconnect()
