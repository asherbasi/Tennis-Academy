from flask import *
from app.department import department_bp
from app.department.models import department
from app.department.forms import DepartmentForm
from app import db

@department_bp.route("/department_list",methods=['GET'])
def get_department_list():
    DEP=department.query.all()
    return render_template("list_department.html", dep=DEP)

@department_bp.route('/add_departments', methods=["GET", "POST"])
def add_departments():
    forms=DepartmentForm()
    if forms.validate_on_submit():
     faculty_id=forms.faculty_id.data
     name=forms.name.data
     code=forms.code.data
     new_department=department(faculty_id=faculty_id,name=name, code=code)
     db.session.add(new_department)
     db.session.commit()
     return redirect (url_for('department.get_department_list'))
    return render_template("add_department.html", fm=forms)

@department_bp.route('/update_department/<int:id>',methods=["GET", "POST"])
def update_department(id):
   DEP=department.query.get_or_404(id)
   form=DepartmentForm(obj=DEP)
   if form.validate_on_submit():
        form.populate_obj(DEP)
        db.session.commit()
        return redirect(url_for("department.get_department_list"))
   return render_template('add_department.html', fm=form)

@department_bp.route('/delete_department/<int:id>', methods=['POST'])
def delete_department(id):
    DP=department.query.get_or_404(id)
    db.session.delete(DP)
    db.session.commit()
    return redirect (url_for('department.get_department_list'))

@department_bp.route('/delete_all_department/', methods=['POST'])
def delete_all_department():
    department.query.delete()
    db.session.commit()
    return redirect (url_for('department.get_department_list'))

print("Hello World")

