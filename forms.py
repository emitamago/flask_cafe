"""Forms for Flask Cafe."""

from wtforms import SelectField, StringField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Optional, URL, Email, ValidationError
from flask_wtf import FlaskForm

#########################################
#helper methods

def input_length_check(form, field):
    if len(field.data) > 6:
        raise ValidationError(f'Must be more than 6 characters')

########################################

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


class SignupForm (FlaskForm):
    """form for user to sign up """
    username = StringField(
                        "username",
                        validators=[InputRequired()]
                        )
    first_name = StringField(
                        "first_name",
                        validators=[InputRequired()]
    )

    last_name = StringField(
                    "last_name",
                    validators=[InputRequired()]
    )   

    description = TextAreaField(
                    "description",
                    validators=[Optional()]
    )   

    email = StringField(
                    "email",
                    validators=[InputRequired(), Email()]
    ) 

    hashed_password = PasswordField(
                    "password",
                    validators=[InputRequired(), input_length_check]
    )

    image_url = StringField(
                        "image_url",
                        validators=[Optional(), URL()]
    )   


class LoginForm(FlaskForm):
    """form to for user to log in  """

    username = StringField(
                        "username",
                        validators=[InputRequired()]
    )

    password = PasswordField(
                        "password",  
                        validators=[InputRequired(), input_length_check]
    )









