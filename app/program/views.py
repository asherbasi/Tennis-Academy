from flask import *
from app.program import program_bp
from app.program.models import program
from app.program.forms import ProgramForm
from app import db

@program_bp.route("/program_list", methods=['GET'])
def get_program_list():
    Program=program.query.all()
    return render_template("list_program.html", prog=Program)

@program_bp.route('/add_program', methods=["GET", "POST"])
def add_program():
    forms=ProgramForm()
    if forms.validate_on_submit():
        department_id=forms.department_id.data
        name=forms.program_name.data
        code=forms.program_code.data
        new_program=program(department_id=department_id,name=name, code= code)
        db.session.add(new_program)
        db.session.commit()
        return redirect (url_for('program.get_program_list'))
    
    return render_template("add_programs.html", form=forms)


@program_bp.route('/update_program/<int:id>',methods=["GET", "POST"])
def update_program(id):
    Program=program.query.get_or_404(id)
    form=ProgramForm(obj=Program)
    if form.validate_on_submit():
        form.populate_obj(program)
        db.session.commit()
        return redirect(url_for("program.get_program_list"))
    return render_template('add_programs.html', form=form)

@program_bp.route('/delete_program/<int:id>', methods=['POST'])
def delete_program(id):
     Program=program.query.get_or_404(id)
     db.session.delete(Program)
     db.session.commit()
     return redirect (url_for('program.get_program_list'))

@program_bp.route('/delete_all_program/', methods=['POST'])
def delete_all_program():
    program.query.delete()
    db.session.commit()
    return redirect (url_for('program.get_program_list'))
