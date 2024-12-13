from flask import *
from app.course import course_bp

@course_bp.route('/course_list')
def get_course_list():
    return render_template('list_course.html')


