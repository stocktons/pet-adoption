"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):
    """ Form for adding pets. """

    name = StringField("Pet name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat','Cat'),
                                              ('dog','Dog'),
                                              ('porcupine','Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField("Age", choices=[('baby','Baby'),
                                     ('young','Young'),
                                     ('adult','Adult'),
                                     ('senior','Senior')])
    notes = TextAreaField("Notes")

class EditPetForm(FlaskForm):
    """ Form for editing pets. """

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    available = BooleanField("Is Available")
    notes = TextAreaField("Notes")
