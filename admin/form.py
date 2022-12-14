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
class ShopsForm(FlaskForm):
    name = StringField('name')
    time = StringField('time')
    location = StringField('location')
    wpLink = StringField('wpLink')
    instaLink = StringField('instaLink')
    map = StringField('map')
    order = IntegerField('order')
    is_active = BooleanField('is_active')
    submit = SubmitField('Submit')

# Lahiyənin Menu bölməsinin formunun qurulması

class MenuForm(FlaskForm):
    name = StringField('name')
    order = IntegerField('order')
    submit = SubmitField('Daxil et')
    
class MenuItemsForm(FlaskForm):
    names = StringField('name')
    price = IntegerField('price')
    info = StringField('info')
    img = FileField('img')
    submit = SubmitField('Daxil et')

# Lahiyənin Şef bölməsinin Formunun yaradılması
class MemberForm(FlaskForm):
    name = StringField('name')
    profession = StringField('profession')
    img = FileField('img')
    info = StringField('info')
    submit = SubmitField('submit')
    



class EventsForm(FlaskForm):
    title = StringField('title')
    price = IntegerField('price')
    info = CKEditorField('info')
    img = FileField('img')

# Lahiyənin About bölməsinin Formunun yaradılması

class AboutForm(FlaskForm):
    img = FileField('img')
    
class RecommendsForm(FlaskForm):
    number = IntegerField('number')
    title = StringField('title')
    text = StringField('text')
    
# Lahiyənin baş hissəsi
class TopBarForm(FlaskForm):
    number = StringField('number')
    date = StringField('date')
    whatsappLink = StringField('wLink')
    instagramLink = StringField('Ilink')
    tiktokLink = StringField('Tlink')
    submit = SubmitField('submit')
    
class EnjoyForm(FlaskForm):
    name = StringField('name')
    price = StringField('price')
    info = StringField('info')
    info2 = StringField('info2')
    info3 = StringField('info3')
    img = FileField('img')
    submit = SubmitField('Daxil et')
    
class PodsForm(FlaskForm):
    price = IntegerField('price')
    info = StringField('info')
    info2 = StringField('info')
    img = FileField('img')
    submit = SubmitField('Daxil et')