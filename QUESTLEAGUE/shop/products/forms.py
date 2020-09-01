from wtforms import Form, SubmitField,IntegerField,FloatField,StringField,TextAreaField,validators,PasswordField,validators, ValidationError, SelectField
from flask_wtf.file import FileField,FileRequired,FileAllowed

from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet

class Addproducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = FloatField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    size = SelectField ('Size', [validators.DataRequired()], choices=[( 'XS','Extra Small'), ('S','Small'), ('M','Medium'),('L','Large'),('XL','Extra Large')])
    colors = StringField('Colors', [validators.DataRequired()])
    discription = TextAreaField('Discription', [validators.DataRequired()])

    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])
    image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])



class MyForm(FlaskForm):
    image = FileField('image')