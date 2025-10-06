# models/course.py

class Course:
    def __init__(self, course_id=None, course_name=None, faculty_name=None):
        self.course_id = course_id
        self.course_name = course_name
        self.faculty_name = faculty_name
