from run import db,main


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

class Testimonials(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    profession = db.Column(db.String(200))
    img = db.Column(db.String(200))
    info = db.Column(db.String(255))
    order = db.Column(db.Integer)
    is_active  = db.Column(db.Boolean)
    
# Lahiyənin Menyu bölməsinin model hissəsinin qurulması
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    order = db.Column(db.Integer)
    categories = db.relationship('CategoryItems', backref='category', lazy=True)

class CategoryItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    info = db.Column(db.String(120))
    price = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

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

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(150))
    passward = db.Column(db.String(100))
    info = db.Column(db.Text)
    
