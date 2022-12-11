import numbers
from run import db,main,ma
from flask_login import UserMixin
class Product(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(180))
    productPrice = db.Column(db.Integer)
    producutInfo = db.Column(db.String(200))
    
class Navlinks(db.Model):
    id=db.Column(db.Integer,primary_key =True)
    nav_Name = db.Column(db.String(200))
    nav_URL = db.Column(db.String(200))
    nav_order = db.Column(db.Integer)
    is_active = db.Column(db.Boolean)

class Shops(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    location = db.Column(db.String(255))
    time = db.Column(db.String(200))
    wpLink = db.Column(db.String(255))
    instaLink = db.Column(db.String(255))
    map = db.Column(db.String(255))
    order = db.Column(db.Integer)
    is_active  = db.Column(db.Boolean)
    
# Lahiyənin Menyu bölməsinin model hissəsinin qurulması
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    order = db.Column(db.Integer)
    categories = db.relationship('CategoryItems', backref='category', lazy=True)
    categories2 = db.relationship('PodsItems', backref='category', lazy=True)
# class CategorySchema(ma.SQLAlchemySchema):
#     class Meta:
#         model:Category
#         fields = ("id","name")
#         include_relationship = True
    

class CategoryItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    info = db.Column(db.String(120))
    price = db.Column(db.Integer)
    img = db.Column(db.String(200))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    
class PodsItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    info = db.Column(db.String(200))
    info2 = db.Column(db.String(200)) 
    img = db.Column(db.String(200))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
# class CategoryItemsSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model:CategoryItems
#         fields = ("id","name","category_id")
#         include_relationship = True

# Lahiyənin Şef bölməsinin  Modelinin yaradılması
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    profession = db.Column(db.String(100))
    img = db.Column(db.String(100))
    info = db.Column(db.Text)
    images = db.relationship('MemberImg', backref='member', lazy=True)
    
class MemberImg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))

# Saytda Qeydiyatdan Keçən İstifadəçilərin Məlumatlarının Modeli

class Users(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(150))
    passward = db.Column(db.String(100))
    info = db.Column(db.Text)
    is_active = db.Column(db.Boolean())
    
# Events section 

class Events(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(120))
    price = db.Column(db.Integer)
    info = db.Column(db.Text)
    img = db.Column(db.String(100))
   
# About section  

class Abouts(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    img = db.Column(db.String(100))
    
class Recommends(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    number = db.Column(db.Integer)
    title = db.Column(db.String(150))
    text = db.Column(db.String(200))
    
class TopBar(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    number = db.Column(db.Integer)
    date = db.Column(db.String(200))
    wpLink = db.Column(db.String(200))
    insLink = db.Column(db.String(200))
    tikLink = db.Column(db.String(200))
    
class Enjoy(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    price = db.Column(db.String(200))
    info = db.Column(db.String(200))
    info2 = db.Column(db.String(200))
    info3 = db.Column(db.String(200))
    img = db.Column(db.String(200))
    