from flask import render_template
from app import app_bp

@app_bp.route('/')
def index():
    from model import Navlinks,Category,CategoryItems,Member,TopBar,Enjoy,Shops
    navlinks = Navlinks.query.filter_by(is_active=True).order_by(Navlinks.nav_order).all()
    menu = Category.query.order_by(Category.order).all()
    menuElements = CategoryItems.query.all()
    members = Member.query.all()
    topbar = TopBar.query.all()
    enjoy = Enjoy.query.all()
    shops=Shops.query.all()
    return render_template('app/index.html',navlinks=navlinks,menu=menu,menuElements=menuElements,CategoryItems=CategoryItems,members=members,topbar=topbar,enjoy=enjoy,shops=shops)

@app_bp.route('/members/images/<id>')
def member_img(id):
    from model import MemberImg,Member
    members = Member.query.get(id)
    memberImgs = MemberImg.query.filter_by(member_id=id).all()
    return render_template('app/membersImg.html',membersImgs=memberImgs,members=members)
    

@app_bp.route('/liquids')
def liquids():
    from model import Navlinks,Category,CategoryItems,Member,TopBar,Enjoy
    navlinks = Navlinks.query.filter_by(is_active=True).order_by(Navlinks.nav_order).all()
    menu = Category.query.order_by(Category.order).all()
    menuElements = CategoryItems.query.all()
    members = Member.query.all()
    topbar = TopBar.query.all()
    enjoy = Enjoy.query.all()
    return render_template('app/liquids.html',navlinks=navlinks,menu=menu,menuElements=menuElements,CategoryItems=CategoryItems,members=members,topbar=topbar,enjoy=enjoy)


@app_bp.route('/products')
def products():
    from model import Navlinks,Category,CategoryItems,Member,TopBar,Enjoy
    navlinks = Navlinks.query.filter_by(is_active=True).order_by(Navlinks.nav_order).all()
    menu = Category.query.order_by(Category.order).all()
    menuElements = CategoryItems.query.all()
    members = Member.query.all()
    topbar = TopBar.query.all()
    enjoy = Enjoy.query.all()
    return render_template('app/products.html',navlinks=navlinks,menu=menu,menuElements=menuElements,CategoryItems=CategoryItems,members=members,topbar=topbar,enjoy=enjoy)


@app_bp.route('/pods')
def pods():
    from model import Navlinks,Category,PodsItems,Member,TopBar,Enjoy
    navlinks = Navlinks.query.filter_by(is_active=True).order_by(Navlinks.nav_order).all()
    menu = Category.query.order_by(Category.order).all()
    menuElements = PodsItems.query.all()
    members = Member.query.all()
    topbar = TopBar.query.all()
    enjoy = Enjoy.query.all()
    return render_template('app/pods.html',navlinks=navlinks,menu=menu,menuElements=menuElements,members=members,topbar=topbar,enjoy=enjoy)
