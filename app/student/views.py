from flask import *
from app.student import student_bp

@student_bp.route('/student_list')
def get_student_list():
    return render_template('list_student.html')

