from flask import *
from app.assign_student import assign_student_bp

@assign_student_bp.route('/assign_student_list')
def get_assign_student_list():
    return render_template('list_assign_student.html')