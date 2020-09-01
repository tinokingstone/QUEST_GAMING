from wtforms import Form, StringField, TextAreaField, PasswordField,SubmitField,validators, ValidationError
from flask_wtf.file import FileRequired,FileAllowed, FileField
from flask_wtf import FlaskForm
from .model import Register


class CustomerRegisterForm(FlaskForm):
    FirstName = StringField('')
    SecondName = StringField('')
    username = StringField('', [validators.DataRequired()])
    email = StringField('', [validators.Email(), validators.DataRequired()])
    password = PasswordField('', [validators.DataRequired(), validators.EqualTo('confirm', message=' Both password must match! ')])
    confirm = PasswordField('', [validators.DataRequired()])

    profile = FileField('Profile', validators=[FileAllowed(['jpg','png','jpeg','gif'], 'Image only please')])
    submit = SubmitField('SIGN UP')

    def validate_username(self, username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError("Please try another name, this username is already in use!")
        
    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError("This email address is already in use!")


class GtagActivision(FlaskForm):
    gtag_activision = StringField('')
    submit = SubmitField('UPDATE')

class GtagPs4(FlaskForm):
    gtag_ps4 = StringField('')
    submit = SubmitField('UPDATE')

class GtagXbox(FlaskForm):
    gtag_xbox = StringField('')
    submit = SubmitField('UPDATE')

class GtagUnreal(FlaskForm):
    gtag_unreal = StringField('')
    submit = SubmitField('UPDATE')

    

class CustomerLoginFrom(FlaskForm):
    email = StringField('', [validators.Email(), validators.DataRequired()])
    password = PasswordField('', [validators.DataRequired()])

    submit = SubmitField('LOGIN')

   




   

 

    

     

   


    

