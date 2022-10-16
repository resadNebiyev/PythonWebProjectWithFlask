from genericpath import isdir
from re import template
from admin.routes import *
import os
# Admin tərəfinə giriş və çıxış 


@admin_bp.route('/')
@login_required
def index():
    from model import Users
    context = {
        'title':'Admin Panel',
        'user' : current_user,
        'users': Users.query.all(),
        }
    return render_template('admin/index.html',**context)

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/auth/')

@admin_bp.route('/user/approve/<id>')
@login_required
def approve(id):
    from model import Users,db
    user = Users.query.filter_by(id=id).first()
    user.is_active=True
    db.session.commit()
    return redirect('/')
# Admin hissəsinin product routu
@admin_bp.route('/product/',methods=['GET','POST'])
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
                path = f"C:\\Users\\user\\Documents\\PythonWebProjectWithFlasks\\static\\uploads"
                os.chdir(path)
                new_folder = 'Testimonials'
                new_folder_path = f'C:/Users/user/Documents/PythonWebProjectWithFlasks/static/uploads/{new_folder}/'
                if os.path.exists(new_folder_path)!=True:
                    os.mkdir(new_folder)
                file.save(os.path.join(f'C:/Users/user/Documents/PythonWebProjectWithFlasks/static/uploads/{new_folder}/',new_filename))
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

@admin_bp.route('/testimonials/delete/<id>',methods=['GET','POST'])
def testimonials_del(id):
    from run import db,main
    from model import Testimonials
    query = Testimonials.query.get(id)
    db.session.delete(query)
    db.session.commit()
    return redirect(url_for('admin.testimonials'))
    
# Lahiyənin Menu bölməsinin Hazırlanması

@admin_bp.route('/menu',methods=['GET','POST'])
def menu():
    from model import db,Category
    categories = Category.query.all()
    from admin.form import MenuForm
    myForm=MenuForm()
    if request.method=='POST':
        name = myForm.name.data
        category = Category(name=name)
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

# Lahiyənin Menu bölməsinin Elementlərinin edit edilməsi

@admin_bp.route('/menu-items/edit/<id>',methods=['GET','POST'])
def edit_menu(id):
    from admin.form import MenuItemsForm
    myForms = MenuItemsForm()
    from model import CategoryItems,Category,db
    menu_categories = Category.query.all()
    query = CategoryItems.query.get(id)
    if request.method =='POST':
        categoryId = request.form.get('category')
        query.name=myForms.names.data
        query.info=myForms.price.data
        query.price=myForms.info.data
        query.category_id=categoryId
        db.session.commit()
        return redirect('/admin/menu-items')
    return render_template('admin/menuItemsEdit.html',query=query,myForms=myForms,menu_categories=menu_categories)
    
# Lahiyənin Menu bölməsinin Silinməsi

@admin_bp.route('/menu/delete/<id>',methods=['GET','POST'])
def menu_delete(id):
    from model import Category,db,CategoryItems
    query = Category.query.get(id)
    query2 = CategoryItems.query.filter_by(category_id=id).first()
    db.session.delete(query)
    if query2:
        db.session.delete(query2)
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
        path = f"C:\\Users\\user\\Documents\\PythonWebProjectWithFlasks\\static\\uploads"
        os.chdir(path)
        new_folder = f'{name}'
        os.mkdir(new_folder)
        file.save(os.path.join(f"C:\\Users\\user\\Documents\\PythonWebProjectWithFlasks\\static\\uploads\\{new_folder}",new_filename))
        img = new_filename
        member_data = Member(name=name,profession=profession,img=img,info=info)
        db.session.add(member_data)
        db.session.commit()
        return redirect('/admin/chefs')
    return render_template('admin/ChefMembers.html',member=member,members=members)

# Lahiyənin Şef bölməsinin Üzvlərinin Tam Silinməsi

@admin_bp.route('/chefs/edit/<id>',methods=['GET','POST'])
def chefs_edit(id):
    from model import Member,db
    from admin.form import MemberForm
    member = MemberForm()
    members = Member.query.get(id)
    if request.method=='POST':
        members.name = member.name.data
        members.profession = member.profession.data
        members.info = member.info.data
        file = request.files['img']
        filename = secure_filename(file.filename)
        extension = filename.rsplit('.',1)[1]
        new_filename = f'Member-{random.randint(1,100)}.{extension}'
        path = f"C:\\Users\\user\\Documents\\PythonWebProjectWithFlasks\\static\\uploads"
        os.chdir(path)
        if os.path.exists("{path}/{members.name}"):
            file.save(os.path.join(f"C:\\Users\\user\\Documents\\PythonWebProjectWithFlasks\\static\\uploads\\{members.name}",new_filename))
        else:
            new_folder = f'{members.name}'
            os.mkdir(new_folder)
            file.save(os.path.join(f"C:\\Users\\user\\Documents\\PythonWebProjectWithFlasks\\static\\uploads\\{members.name}",new_filename))
        members.img = new_filename
        db.session.commit()
        return redirect('/admin/chefs')
    return render_template('/admin/editChefs.html',member=member,members=members) 


# Lahiyənin Şef bölməsinin Üzvlərinin Tam Silinməsi

@admin_bp.route('/chefs/delete/<id>',methods=['GET','POST'])
def chefs_delete(id):
    from model import Member,db
    member = Member.query.get(id)
    # os.rmdir(f"C:\\Users\\user\\Documents\\PythonWebProjectWithFlask\\admin\\static\\uploads\\{member.name}")
    db.session.delete(member)
    db.session.commit()
    return redirect('/admin/chefs')

# Lahiyənin Şef bölməsinin Üzvlərinin Şəkillərinin əlavə edilməsi

