from flask import render_template,request,redirect
from admin import admin_bp
from werkzeug.utils import secure_filename
import os
import random

from admin.form import MenuItemsForm
from model import Member

# Admin tərəfinə giriş

@admin_bp.route('/')
def index():
    return render_template('admin/index.html')

# Admin hissəsinin product routu

@admin_bp.route('/product',methods=['GET','POST'])
def product():
    from model import db,Product
    from admin.form import Products
    products = Products()
    data = Product.query.all()
    if request.method =='POST':
        productName = products.productName.data
        productPrice = products.productPrice.data
        productInfo = products.productInfo.data
        productM=Product(productName=productName,productPrice=productPrice,producutInfo=productInfo)
        db.session.add(productM)
        db.session.commit()
        return redirect('/admin/product')
    return render_template('admin/product.html',products=products,data=data)

# Product hissəsinin edit edilməsi

@admin_bp.route('/product/edit/<id>',methods=['GET','POST'])
def edit(id):
    from admin.form import Products
    product = Products()
    from model import Product,db
    data = Product.query.get(id)
    if request.method=='POST':
        data.productName=product.productName.data
        data.productPrice=product.productPrice.data
        data.producutInfo=product.productInfo.data
        db.session.commit()
        return redirect('/admin/product')
    return render_template('admin/update.html',product=product,data=data)

# Product hissəsinin silinməsi

@admin_bp.route('/product/delete/<id>')
def delete(id):
    from model import Product,db
    data = Product.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/admin/product')

#  navbar hissəsindəki datalar üzərində əməliyyatlar

@admin_bp.route('/navlinks',methods=['GET','POST'])
def navlinks():
    from model import Navlinks,db
    from admin.form import NavLinksForm
    navLinksForm = NavLinksForm()
    navlinks = Navlinks.query.all()
    if request.method=='POST':
        name = navLinksForm.name.data
        url = navLinksForm.url.data
        order = navLinksForm.order.data
        is_active = navLinksForm.is_active.data
        navlinks = Navlinks(nav_Name=name,nav_URL=url,nav_order=order,is_active=is_active)
        db.session.add(navlinks)
        db.session.commit()
        return redirect('/admin/navlinks')
    return render_template('admin/navbarform.html',navLinksForm=navLinksForm,navlinks=navlinks)

@admin_bp.route('/navlinks/edit/<id>',methods=['GET','POST'])
def edit_navlinks(id):
    from admin.form import NavLinksForm
    from model import Navlinks,db
    query = Navlinks.query.get(id)
    navlinks = NavLinksForm()
    if request.method=='POST':
        query.nav_Name = navlinks.name.data
        query.nav_URL= navlinks.url.data
        query.nav_order = navlinks.order.data
        query.is_active = navlinks.is_active.data
        db.session.commit()
        return redirect('/admin/navlinks')
    return render_template('admin/updateform.html',navlinks=navlinks,query=query)

@admin_bp.route('/navlinks/delete/<id>')
def delete_navLinks(id):
        from model import Navlinks,db
        query=Navlinks.query.get(id)
        db.session.delete(query)
        db.session.commit()
        return redirect('/admin/navlinks')


# Lahiyənin "Testimonials" hissəsinin hazırlanması

@admin_bp.route('/testimonials',methods=['GET','POST'])
def testimonials():
    from run import db,main
    from model import Testimonials
    from admin.form import testimonialForm
    myForm =testimonialForm()
    data = Testimonials.query.all()
    if request.method=="POST" :
        file = request.files['img']           # inputdan fayl götürmək('img' inputun name atributudur)
        if file:                              # əgər fayl seçilibsə :
            main.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024   # (Max size 16 MB ola bilər)
            main.config['ALLOWED_EXTENSIONS'] = ['jpg','png']      
            filename = secure_filename(file.filename)
            extension = filename.rsplit('.',1)[1]
            new_filename = f'testimonials_photo-{random.randint(1,100)}.{extension}'
            if extension in main.config['ALLOWED_EXTENSIONS']:
                file.save(os.path.join('/static/uploads/',new_filename))
                name=myForm.name.data
                info=myForm.info.data
                profession=myForm.profession.data
                order=myForm.order.data
                img=new_filename                  # Testimonials modelinin img sütununa faylın adıının yazılması
                is_active=myForm.is_active.data
                testimonial=Testimonials(name=name,info=info,order=order,is_active=is_active,profession=profession,img=img)
                db.session.add(testimonial)
                db.session.commit()
                return redirect('/admin/testimonials')
    return render_template('admin/testimonials.html',myForm=myForm,data=data)

# Lahiyənin Menu bölməsinin Hazırlanması

@admin_bp.route('/menu',methods=['GET','POST'])
def menu():
    from model import db,Category
    categories = Category.query.all()
    from admin.form import MenuForm
    myForm=MenuForm()
    if request.method=='POST':
        name = myForm.name.data
        order = myForm.order.data
        category = Category(name=name,order=order)
        db.session.add(category)
        db.session.commit()
        return redirect('/admin/menu')
    return render_template('admin/menu.html',myForm=myForm,categories=categories)

# Lahiyənin Menu bölməsinin Elementlərinin Hazırlanması

@admin_bp.route('/menu-items',methods=['GET','POST'])
def menuItems():
    from admin.form import MenuItemsForm
    from model import  Category,CategoryItems,db
    menu_categories = Category.query.all()
    categories = CategoryItems.query.all()
    myForm = MenuItemsForm()
    if request.method =='POST':
        name = myForm.names.data
        info = myForm.info.data
        price=myForm.price.data
        categoryId = request.form.get('category')
        item = CategoryItems(name=name,info=info,price=price,category_id=categoryId)
        db.session.add(item)
        db.session.commit()
        print(categoryId)
        return redirect('/admin/menu-items')
    return render_template('admin/menu-items.html',myForms=myForm,categories=categories,menu_categories=menu_categories)

# Lahiyənin Menu bölməsinin Silinməsi

@admin_bp.route('/menu/delete/<id>',methods=['GET','POST'])
def menu_delete(id):
    from model import Category,db
    query = Category.query.get(id)
    db.session.delete(query)
    db.session.commit()
    return redirect('/admin/menu')

# Lahiyənin Menu bölməsinin Elementlərinin Silinməsi

@admin_bp.route('/menu-items/delete/<id>',methods=['GET','POST'])
def menu_delete_items(id):
    from model import CategoryItems,db
    query = CategoryItems.query.get(id)
    db.session.delete(query)
    db.session.commit()
    return redirect('/admin/menu-items')

# Lahiyənin Şef bölməsinin  Hazırlanması

@admin_bp.route('/chefs',methods=['GET','POST'])
def chefs():
    from model import Member,db
    from admin.form import MemberForm
    member = MemberForm()
    members = Member.query.all()
    if request.method=='POST':
        name = member.name.data
        profession = member.profession.data
        info = member.info.data
        file = request.files['img']
        filename = secure_filename(file.filename)
        extension = filename.rsplit('.',1)[1]
        new_filename = f'Member-{random.randint(1,100)}.{extension}'
        path = f"C:\\Users\\user\\Documents\\PythonWebProjectWithFlask\\static\\uploads"
        os.chdir(path)
        new_folder = f'{name}'
        os.mkdir(new_folder)
        file.save(os.path.join(f"C:\\Users\\user\\Documents\\PythonWebProjectWithFlask\\static\\uploads\\{new_folder}",new_filename))
        img = new_filename
        member_data = Member(name=name,profession=profession,img=img,info=info)
        db.session.add(member_data)
        db.session.commit()
        return redirect('/admin/chefs')
    return render_template('admin/ChefMembers.html',member=member,members=members)

# Lahiyənin Şef bölməsinin Üzvlərinin Tam Silinməsi

@admin_bp.route('/chefs/delete/<id>',methods=['GET','POST'])
def chefs_delete(id):
    from model import Member,db
    member = Member.query.get(id)
    # os.rmdir(f"C:\\Users\\user\\Documents\\PythonWebProjectWithFlask\\admin\\static\\uploads\\{member.name}")
    db.session.delete(member)
    db.session.commit()
    return redirect('/admin/chefs')
    
@admin_bp.route('/chefs/images')
def chefs_images():
    from model import Member,MemberImg
    from admin.form import MemberİmgForm
    memberForm = MemberİmgForm()
    members = Member.query.all()
    memberImgs = MemberImg.query.all()
    return render_template('admin/MemberImg.html',members=members,memberForm=memberForm,memberImgs=memberImgs)
    