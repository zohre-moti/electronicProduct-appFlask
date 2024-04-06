from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange, Optional
from app.models import Product, UserComments

class ProductForm(FlaskForm):
    name = StringField('نام محصول', validators=[DataRequired()])
    description = TextAreaField('توضیحات')
    price = FloatField('قیمت', validators=[DataRequired(), NumberRange(min=0)])
    quantity = IntegerField('موجودی', validators=[DataRequired(), NumberRange(min=0)])



class UserCommentsForm(FlaskForm):
    comment = TextAreaField('نظر', validators=[DataRequired()])
    rating = SelectField('امتیاز', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])

 
