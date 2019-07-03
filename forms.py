"""Forms for Flask Cafe."""

from wtforms import SelectField, StringField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL
from flask_wtf import FlaskForm

class AddEditCafeForm(FlaskForm):
    """ form for adding and editting a cafe """
    
    name = StringField(
                        "name",
                        validators=[InputRequired()]
                        )
    description = TextAreaField(
                        "description",
                        validators=[Optional()]
    )

    url = StringField(
                    "url",
                    validators=[Optional(), URL()]
    )   

    address = StringField(
                    "address",
                    validators=[InputRequired()]
    )   

    city_code = SelectField("city_code")

    image_url = StringField(
                        "imageurl",
                        validators=[Optional(), URL()]
    )   