from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,IntegerField,BooleanField,FileField,SelectField
from flask_ckeditor import CKEditorField
class Products(FlaskForm):
    productName = StringField('name')
    productPrice = StringField('price')
    productInfo = CKEditorField()
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
    info = CKEditorField('info')
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
    info = CKEditorField('info')
    submit = SubmitField('submit')

# Lahiyənin Şef bölməsinin Formunun yaradılması
class MemberForm(FlaskForm):
    name = StringField('name')
    profession = StringField('profession')
    img = FileField('img')
    info = CKEditorField('info')
    submit = SubmitField('submit')
    
# Lahiyənin Şef bölməsinin Şəkillərinin Formunun yaradılması

class MemberİmgForm(FlaskForm):
    cat = SelectField('cat',choices=[])
    img = FileField('img')
    submit = SubmitField('Add')


class EventsForm(FlaskForm):
    title = StringField('title')
    price = IntegerField('price')
    info = CKEditorField('info')
    img = FileField('img')
