from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Optional, Email

class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField("Name", validators=
                      [InputRequired(message="Pet name can't be blank.")])
    
    species = StringField("Species", validators=
                      [InputRequired(message="Species can't be blank.")])
    
    photo_url = StringField("Image URL")

    notes = StringField("About Me", validators=
                        [InputRequired(message="Tell us about our new friend.")])
    
    