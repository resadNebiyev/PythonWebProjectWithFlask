from re import I
from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,IntegerField,BooleanField,FileField

class Products(FlaskForm):
    productName = StringField('name')
    productPrice = StringField('price')
    productInfo = TextAreaField()
    productSub = SubmitField('Submit')

class NavLinksForm(FlaskForm):
    name = StringField('name')
    url = StringField('url')
    order = IntegerField('order')
    is_active = BooleanField('is_active')
    submit = SubmitField('Submit')

# Lahiyənin 'Testimonials' hissəsinin formunun yaradilması
class testimonialForm(FlaskForm):
    name = StringField('name')
    profession = StringField('profession')
    info = StringField('info')
    order = IntegerField('order')
    img = FileField('img')
    is_active = BooleanField('is_active')
    submit = SubmitField('Submit')

# Lahiyənin Menu bölməsinin formunun qurulması

class MenuForm(FlaskForm):
    name = StringField('name')
    order = IntegerField('order')
    submit = SubmitField('submit')
    
class MenuItemsForm(FlaskForm):
    names = StringField('name')
    price = IntegerField('price')
    info = StringField('info')
    submit = SubmitField('submit')

# Lahiyənin Şef bölməsinin Formunun yaradılması
class MemberForm(FlaskForm):
    name = StringField('name')
    profession = StringField('profession')
    img = FileField('img')
    info = TextAreaField('info')
    submit = SubmitField('submit')
    
# Lahiyənin Şef bölməsinin Şəkillərinin Formunun yaradılması

class MemberİmgForm(FlaskForm):
    img = FileField('img')
    submit = SubmitField('Add')
