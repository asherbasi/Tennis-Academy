from flask import *
from app.faculty import faculty_bp
from app.faculty.forms import FacultyForm
from app import db
from app.faculty.models import faculty

@faculty_bp.route("/faculty_list") #method=['GET'] 
def get_faculty_list():
    mash=faculty.query.all()
    return render_template("list_faculty.html", fac=mash)
#GET- Used to retreive information and pass the information to the html page
#POST - to submit the data
#put - 
#delete - delete or to remove 

@faculty_bp.route('/add_faculty',methods=['GET','POST'])
def add_faculty():
    forms=FacultyForm()
    if forms.validate_on_submit():
        faculty_name= forms.name.data
        faculty_code= forms.code.data
        new_faculty=faculty(name=faculty_name, code= faculty_code)
        db.session.add(new_faculty)
        db.session.commit()
        return redirect(url_for("faculty.get_faculty_list"))
    return render_template("add_faculty.html", form=forms)

@faculty_bp.route("/delete_faculty/<int:id>",methods=['POST'])
def delete_faculty(id):
   mash=faculty.query.get_or_404(id)
   db.session.delete(mash)
   db.session.commit()
   return redirect(url_for('faculty.get_faculty_list'))

@faculty_bp.route('/edit_faculty/<int:id>', methods=["GET", "POST"])
def update_faculty(id):
    mash=faculty.query.get_or_404(id)
    form=FacultyForm(obj=mash)
    if form.validate_on_submit():
        form.populate_obj(mash)
        db.session.commit()
        return redirect(url_for('faculty.get_faculty_list'))
    return render_template('add_faculty.html', form=form)

@faculty_bp.route("/delete_all_faculty",methods=['POST'])
def delete_all_faculty():
   faculty.query.delete()
   db.session.commit()
   return redirect(url_for('faculty.get_faculty_list'))

