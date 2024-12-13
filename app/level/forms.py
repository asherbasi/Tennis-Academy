from flask_wtf import *
from wtforms import *
from wtforms.validators import *

class LevelForm(FlaskForm):
    id=HiddenField('id')
    level_id=IntegerField('Level ID:', validators=[DataRequired()])
    level_name=StringField('Level Name:', validators=[DataRequired()])
    submit=SubmitField("Save Changes")
