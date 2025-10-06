# app.py

from flask import Flask, render_template, request, redirect, url_for, session, send_file
from models.student import Student
from models.feedback_entry import FeedbackEntry
from models.admin import Admin
from db_connection import DatabaseConnection
from exceptions import DuplicateFeedbackError, AuthenticationError, DatabaseConnectionError, FileHandlingError
from logger import Logger
from config import SECRET_KEY, LOG_FILE
import os

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Route: Home → redirect to student login or dashboard
@app.route('/')
def home():
    if 'student_id' in session:
        return redirect(url_for('submit_feedback'))
    if 'admin_id' in session:
        return redirect(url_for('admin_view_feedback'))
    return redirect(url_for('student_login'))

# Student registration
@app.route('/register', methods=['GET', 'POST'])
def student_register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        student = Student()
        try:
            student.register(name, email, password)
            return redirect(url_for('student_login'))
        except DuplicateFeedbackError as e:
            return render_template('student_register.html', error=str(e))
        except Exception as e:
            Logger.write_log(f"Error in student registration: {str(e)}")
            return render_template('student_register.html', error="An error occurred.")
    return render_template('student_register.html')

# Student login
@app.route('/login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        student = Student()
        try:
            student_id, name = student.login(email, password)
            session['student_id'] = student_id
            session['student_name'] = name
            return redirect(url_for('submit_feedback'))
        except AuthenticationError as e:
            return render_template('student_login.html', error=str(e))
        except Exception as e:
            Logger.write_log(f"Error in student login: {str(e)}")
            return render_template('student_login.html', error="An error occurred.")
    return render_template('student_login.html')

# Student feedback submission
@app.route('/submit_feedback', methods=['GET', 'POST'])
def submit_feedback():
    if 'student_id' not in session:
        return redirect(url_for('student_login'))

    # Get courses list
    db = DatabaseConnection()
    try:
        conn = db.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT course_id, course_name, faculty_name FROM courses")
        courses = cursor.fetchall()
    finally:
        if cursor:
            cursor.close()
        db.disconnect()

    if request.method == 'POST':
        course_id = request.form.get('course_id')
        rating = request.form.get('rating')
        comments = request.form.get('comments')
        feedback_entry = FeedbackEntry(student_id=session['student_id'],
                                       course_id=course_id,
                                       rating=rating,
                                       comments=comments)
        student = Student()
        try:
            student.submit_feedback(feedback_entry)
            return render_template('submit_feedback.html', courses=courses, message="Feedback submitted!")
        except DuplicateFeedbackError as e:
            return render_template('submit_feedback.html', courses=courses, error=str(e))
        except Exception as e:
            Logger.write_log(f"Error in submitting feedback: {str(e)}")
            return render_template('submit_feedback.html', courses=courses, error="An error occurred.")
    return render_template('submit_feedback.html', courses=courses)

# Student logout
@app.route('/logout')
def student_logout():
    session.pop('student_id', None)
    session.pop('student_name', None)
    return redirect(url_for('student_login'))

# Admin login
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        admin = Admin()
        try:
            admin_id, uname = admin.login(username, password)
            session['admin_id'] = admin_id
            session['admin_username'] = uname
            return redirect(url_for('admin_view_feedback'))
        except AuthenticationError as e:
            return render_template('admin_login.html', error=str(e))
        except Exception as e:
            Logger.write_log(f"Error in admin login: {str(e)}")
            return render_template('admin_login.html', error="An error occurred.")
    return render_template('admin_login.html')

# Admin view feedback
@app.route('/admin/view_feedback')
def admin_view_feedback():
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))
    admin = Admin()
    try:
        feedback_list = admin.view_feedback()
        return render_template('view_feedback.html', feedbacks=feedback_list)
    except Exception as e:
        Logger.write_log(f"Error in admin viewing feedback: {str(e)}")
        return render_template('view_feedback.html', feedbacks=[], error="Could not fetch feedbacks.")

# Admin download log file
@app.route('/admin/download_logs')
def download_logs():
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))
    try:
        return send_file(LOG_FILE, as_attachment=True)
    except Exception as e:
        Logger.write_log(f"Error in downloading logs: {str(e)}")
        return "Error downloading log file."

if __name__ == "__main__":
    app.run(debug=True)
