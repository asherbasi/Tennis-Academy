from flask import *
from app.group import group_bp

@group_bp.route('/group_list')
def get_group_list():
    return render_template('list_group.html')