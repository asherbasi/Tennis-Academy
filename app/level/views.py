from flask import *
from app.level import level_bp
from app.level.forms import LevelForm
from app import db
from app.level.models import level

@level_bp.route("/level_list")
def get_level_list():
    return render_template("list_level.html")
#GET- Used to retreive information and pass the information to the html page
#POST - to submit the data
#put - 
#delete - delete or to remove 

@level_bp.route('/add_level',methods=['GET','POST'])
def add_level():
    forms=LevelForm()
    if forms.validate_on_submit():
        level_id=forms.level_id.data
        level_name= forms.level_name.data
        new_level=level(id= level_id, name=level_name)
        db.session.add(new_level)
        db.session.commit()
        return redirect(url_for("level.get_level_list"))
    return render_template("add_level.html", form=forms)
