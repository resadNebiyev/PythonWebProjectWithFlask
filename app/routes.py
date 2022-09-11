from flask import render_template
from admin.routes import testimonials
from app import app_bp

@app_bp.route('/')
def index():
    from model import Navlinks,Category,CategoryItems,Member,Testimonials
    navlinks = Navlinks.query.filter_by(is_active=True).order_by(Navlinks.nav_order).all()
    menu = Category.query.order_by(Category.order).all()
    menuElements = CategoryItems.query.all()
    members = Member.query.all()
    testimonials = Testimonials.query.all()
    return render_template('app/index.html',testimonials=testimonials,navlinks=navlinks,menu=menu,menuElements=menuElements,CategoryItems=CategoryItems,members=members)

@app_bp.route('/members/images/<id>')
def member_img(id):
    from model import MemberImg,Member
    members = Member.query.get(id)
    memberImgs = MemberImg.query.filter_by(member_id=id).all()
    return render_template('app/membersImg.html',membersImgs=memberImgs,members=members)

