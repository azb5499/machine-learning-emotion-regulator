from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class UserEmotionDescription(FlaskForm):
    description = StringField("Emotional Description",validators=[DataRequired()])
    submitfield = SubmitField(label="Confirm")