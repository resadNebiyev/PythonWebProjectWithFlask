from admin.routes import *
# Admin tərəfinə giriş və çıxış 


@admin_bp.route('/')
@login_required
def index():
    from model import Users
    context = {
        'title':'Admin Panel',
        'user' : current_user,
        'users': Users.query.offset(1).all()
        }
    return render_template('admin/index.html',**context)

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/auth/login')

#  navbar hissəsindəki datalar üzərində əməliyyatlar

@admin_bp.route('/navlinks',methods=['GET','POST'])
@login_required
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
@login_required
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
@login_required
def delete_navLinks(id):
        from model import Navlinks,db
        query=Navlinks.query.get(id)
        db.session.delete(query)
        db.session.commit()
        return redirect('/admin/navlinks')


# Lahiyənin "Shops" hissəsinin hazırlanması

@admin_bp.route('/shops',methods=['GET','POST'])
@login_required
def shops():
    from run import db,main
    from model import Shops
    from admin.form import ShopsForm
    myForm =ShopsForm()
    data = Shops.query.all()
    if request.method=="POST":     
        name=myForm.name.data
        location=myForm.location.data
        time=myForm.time.data
        wpLink=myForm.wpLink.data
        instaLink=myForm.instaLink.data
        map=myForm.map.data
        order=myForm.order.data
        is_active=myForm.is_active.data
        testimonial=Shops(name=name,location=location,order=order,is_active=is_active,time=time,wpLink=wpLink,instaLink=instaLink,map=map)
        db.session.add(testimonial)
        db.session.commit()
        return redirect('/admin/shops')
    return render_template('admin/testimonials.html',myForm=myForm,data=data)


@admin_bp.route('/shops/edit/<id>',methods=['GET','POST'])
def shops_edit(id):
    from run import db,main
    from model import Shops
    from admin.form import ShopsForm
    myForm =ShopsForm()
    data = Shops.query.get(id)
    if request.method=="POST":     
        data.name=myForm.name.data
        data.location=myForm.location.data
        data.time=myForm.time.data
        data.wpLink=myForm.wpLink.data
        data.instaLink=myForm.instaLink.data
        data.map=myForm.map.data
        data.order=myForm.order.data
        data.is_active=myForm.is_active.data
        db.session.commit()
        return redirect('/admin/shops')
    return render_template('admin/editShops.html',myForm=myForm,data=data)


@admin_bp.route('/shops/delete/<id>',methods=['GET','POST'])
@login_required
def shops_del(id):
    from run import db,main
    from model import Shops
    query = Shops.query.get(id)
    db.session.delete(query)
    db.session.commit()
    return redirect('/admin/shops')
    
# Lahiyənin Kateqoriyalarının Hazırlanması

@admin_bp.route('/menu',methods=['GET','POST'])
@login_required
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



# Lahiyənin  Kateqoriya bölməsinin Elementlərinin Hazırlanması

@admin_bp.route('/menu-items',methods=['GET','POST'])
@login_required
def menuItems():
    from admin.form import MenuItemsForm
    from model import  Category,CategoryItems,db
    menu_categories = Category.query.all()
    categories = CategoryItems.query.all()
    myForm = MenuItemsForm()
    if request.method =='POST':
        file = request.files['img']           # inputdan fayl götürmək('img' inputun name atributudur)
        if file:
            name = myForm.names.data
            info = myForm.info.data
            price=myForm.price.data
            categoryId = request.form.get('category')
            filename = secure_filename(file.filename)
            extension = filename.rsplit('.',1)[1]
            new_filename = f'Liquid-{random.randint(1,100)}.{extension}'
            new_folder = 'Liquids'
            file.save(os.path.join(f'../PythonWebProjectWithFlasks/static/uploads/{new_folder}',new_filename))
            img = new_filename
            item = CategoryItems(name=name,info=info,price=price,category_id=categoryId,img=img)
            db.session.add(item)
            db.session.commit()
            print(categoryId)
            return redirect('/admin/menu-items')
    return render_template('admin/menu-items.html',myForms=myForm,categories=categories,menu_categories=menu_categories)


# POD systems

@admin_bp.route('/pods',methods=['GET','POST'])
@login_required
def PodItems():
    from admin.form import PodsForm
    from model import  Category,PodsItems,db
    menu_categories = Category.query.all()
    categories = PodsItems.query.all()
    myForm = PodsForm()
    if request.method =='POST':
        file = request.files['img']           # inputdan fayl götürmək('img' inputun name atributudur)
        if file:
            info = myForm.info.data
            info2 = myForm.info2.data
            price=myForm.price.data
            categoryId = request.form.get('category')
            filename = secure_filename(file.filename)
            extension = filename.rsplit('.',1)[1]
            new_filename = f'POD-{random.randint(1,100)}.{extension}'
            file.save(os.path.join(f'../PythonWebProjectWithFlasks/static/uploads/PODS',new_filename))
            img = new_filename
            item = PodsItems(info=info,info2=info2,price=price,category_id=categoryId,img=img)
            db.session.add(item)
            db.session.commit()
            print(categoryId)
            return redirect('/admin/pods')
    return render_template('admin/pods.html',myForms=myForm,categories=categories,menu_categories=menu_categories)

@admin_bp.route('/menu-items/edit/<id>',methods=['GET','POST'])
@login_required
def edit_menu(id):
    from admin.form import MenuItemsForm
    myForms = MenuItemsForm()
    from model import CategoryItems,Category,db
    menu_categories = Category.query.all()
    query = CategoryItems.query.get(id)
    if request.method =='POST':
        categoryId = request.form.get('category')
        query.name=myForms.names.data
        query.price=myForms.price.data
        query.info=myForms.info.data
        query.category_id=categoryId          
        db.session.commit()
        return redirect('/admin/menu-items')
    return render_template('admin/menuItemsEdit.html',query=query,myForms=myForms,menu_categories=menu_categories)

@admin_bp.route('/pods/edit/<id>',methods=['GET','POST'])
@login_required
def edit_pods(id):
    from admin.form import PodsForm
    myForms = PodsForm()
    from model import PodsItems,Category,db
    menu_categories = Category.query.all()
    query = PodsItems.query.get(id)
    if request.method =='POST':
        categoryId = request.form.get('category')
        query.price=myForms.price.data
        if myForms.info.data and myForms.info2.data:
            query.info=myForms.info.data
            query.info2=myForms.info2.data
        query.category_id=categoryId
        file = request.files['img'] 
        if file:
            filename = secure_filename(file.filename)
            extension = filename.rsplit('.',1)[1]
            new_filename = f'POD-{random.randint(1,100)}.{extension}'
            file.save(os.path.join(f'../PythonWebProjectWithFlasks/static/uploads/PODS',new_filename))
            query.img = new_filename
        db.session.commit()
        return redirect('/admin/pods')
    return render_template('admin/editPods.html',query=query,myForms=myForms,menu_categories=menu_categories)



# Lahiyənin Menu bölməsinin Silinməsi

@admin_bp.route('/menu/delete/<id>',methods=['GET','POST'])
@login_required
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
@login_required
def menu_delete_items(id):
    from model import CategoryItems,db
    query = CategoryItems.query.get(id)
    db.session.delete(query)
    db.session.commit()
    return redirect('/admin/menu-items')

# Lahiyənin Məhsul Bölməsinin  Hazırlanması

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
        new_folder_path = f'C:/Users/user/Documents/PythonWebProjectWithFlasks/static/uploads/{new_folder}/'
        if os.path.exists(new_folder_path)!=True:
            os.mkdir(new_folder)
        file.save(os.path.join(f"C:\\Users\\user\\Documents\\PythonWebProjectWithFlasks\\static\\uploads\\{new_folder}",new_filename))
        img = new_filename
        member_data = Member(name=name,profession=profession,img=img,info=info)
        db.session.add(member_data)
        db.session.commit()
        return redirect('/admin/chefs')
    return render_template('admin/ChefMembers.html',member=member,members=members)


@admin_bp.route('/chefs/edit/<id>',methods=['GET','POST'])
@login_required
def chefs_edit(id):
    from model import Member,db
    from admin.form import MemberForm
    member = MemberForm()
    members = Member.query.get(id)
    imgs = Member.query.all()
    my_list = []
    file_scr = './static/uploads/Enjoy Vape 5000+/'
    for x in os.listdir(file_scr):
        my_list.append(os.path.basename(x))
    if request.method=='POST':
        members.name = member.name.data
        members.profession = member.profession.data
        members.info = member.info.data
        file = request.files['img']
        if file:
            filename = secure_filename(file.filename)
            extension = filename.rsplit('.',1)[1]
            new_filename = f'Member-{random.randint(1,100)}.{extension}'
            path = f"C:\\Users\\user\\Documents\\PythonWebProjectWithFlasks\\static\\uploads"
            os.chdir(path)
            file.save(os.path.join(f"C:\\Users\\user\\Documents\\PythonWebProjectWithFlasks\\static\\uploads\\Enjoy Vape 5000+",new_filename))
            members.img = new_filename
        else:
            members.img = request.form.get('category')
        db.session.commit()
        return redirect('/admin/chefs')
    return render_template('/admin/editChefs.html',member=member,members=members,imgs=imgs,my_list=my_list) 



@admin_bp.route('/chefs/delete/<id>',methods=['GET','POST'])
@login_required
def chefs_delete(id):
    from model import Member,db
    member = Member.query.get(id)
    # os.rmdir(f"C:\\Users\\user\\Documents\\PythonWebProjectWithFlask\\admin\\static\\uploads\\{member.name}")
    db.session.delete(member)
    db.session.commit()
    return redirect('/admin/chefs')

@admin_bp.route('/pods/delete/<id>',methods=['GET','POST'])
@login_required
def pods_delete(id):
    from model import PodsItems,db
    member = PodsItems.query.get(id)
    # os.rmdir(f"C:\\Users\\user\\Documents\\PythonWebProjectWithFlask\\admin\\static\\uploads\\{member.name}")
    db.session.delete(member)
    db.session.commit()
    return redirect('/admin/pods')
# Lahiyənin Şef bölməsinin Üzvlərinin Şəkillərinin əlavə edilməsi

# Top Bar hissəsinin yazilmasi
@admin_bp.route('/topbar',methods=['GET','POST'])
@login_required
def topbar():
    from model import TopBar,db
    from admin.form import TopBarForm
    TopBarForm = TopBarForm()
    topbar= TopBar.query.all()
    if request.method=='POST':
        number = TopBarForm.number.data
        date = TopBarForm.date.data
        wpLink = TopBarForm.whatsappLink.data
        instaLink = TopBarForm.instagramLink.data
        tiktokLink = TopBarForm.tiktokLink.data
        data = TopBar(number=number,date=date,wpLink=wpLink,insLink=instaLink,tikLink=tiktokLink)
        db.session.add(data)
        db.session.commit()
        return redirect('/admin/topbar')
    return render_template('/admin/topbar.html',myForm=TopBarForm,topbar=topbar)

# Top Bar hissəsinin edit olunması
@admin_bp.route('/topbar/update/<id>',methods=['GET','POST'])
@login_required
def topbar_edit(id):
    from admin.form import TopBarForm
    myForms = TopBarForm()
    from model import TopBar,db
    query = TopBar.query.get(id)
    if request.method =='POST':
        query.number = myForms.number.data
        query.date = myForms.date.data
        query.wpLink = myForms.whatsappLink.data
        query.insLink = myForms.instagramLink.data
        query.tikLink = myForms.tiktokLink.data
        db.session.commit()
        return redirect('/admin/topbar')
    return render_template('admin/topbarEdit.html',myForms=myForms,query=query)


@admin_bp.route('/topbar/delete/<id>',methods=['GET','POST'])
@login_required
def topbar_delete(id):
    from model import TopBar,db
    query = TopBar.query.get(id)
    db.session.delete(query)
    db.session.commit()
    return redirect('/admin/topbar')

# Lahiyənin Reklam hissəsinin yazılması

@admin_bp.route('/enjoy',methods=['GET','POST'])
@login_required
def enjoy():
    from model import Enjoy,db
    from admin.form import EnjoyForm
    myForm = EnjoyForm()
    enjoy= Enjoy.query.all()
    if request.method=='POST':
        file = request.files['img']           # inputdan fayl götürmək('img' inputun name atributudur)
        if file:
            name = myForm.name.data
            price = myForm.price.data
            info = myForm.info.data
            info2 = myForm.info2.data
            info3 = myForm.info3.data
            filename = secure_filename(file.filename)
            extension = filename.rsplit('.',1)[1]
            new_filename = f'ENJOY-{random.randint(1,100)}.{extension}'
            path = f"/PythonWebProjectWithFlasks/static/uploads"
            # os.chdir(path)
            new_folder = 'Enjoy'
            new_folder_path = f'./PythonWebProjectWithFlasks/static/uploads/{new_folder}/'
            # if os.path.exists(new_folder_path)==True:
            #     os.mkdir(new_folder)
            file.save(os.path.join(f'../PythonWebProjectWithFlasks/static/uploads/{new_folder}',new_filename))
            img = new_filename
            data = Enjoy(name=name,price=price,info=info,info2=info2,info3=info3,img=img)
            db.session.add(data)
            db.session.commit()
        return redirect('/admin/enjoy')
    return render_template('/admin/enjoy.html',myForm=myForm,data=enjoy)

@admin_bp.route('/enjoy/edit/<id>',methods=['GET','POST'])
@login_required
def enjoy_edit(id):
    from model import Enjoy,db
    from admin.form import EnjoyForm
    myForm = EnjoyForm()
    enjoy= Enjoy.query.get(id)
    allEnjoy = Enjoy.query.all()
    my_list = []
    file_scr = './static/uploads/Enjoy/'
    for x in os.listdir(file_scr):
        my_list.append(os.path.basename(x))
    if request.method=='POST':
        enjoy.name = myForm.name.data
        enjoy.price = myForm.price.data
        enjoy.info = myForm.info.data
        enjoy.info2 = myForm.info2.data
        enjoy.info3 = myForm.info3.data
        enjoy.img = request.form.get('category')
        file = request.files['img']
        if file:
            filename = secure_filename(file.filename)
            extension = filename.rsplit('.',1)[1]
            new_filename = f'ENJOY-{random.randint(1,100)}.{extension}'
            file.save(os.path.join(f'../PythonWebProjectWithFlasks/static/uploads/Enjoy',new_filename))
            enjoy.img = new_filename
        else:
            enjoy.img = request.form.get('category')
        db.session.commit()
        return redirect('/admin/enjoy')
    return render_template('/admin/editEnjoy.html',myForm=myForm,data=enjoy,allEnjoy=allEnjoy,my_list=my_list) 



@admin_bp.route('/enjoy/delete/<id>',methods=['GET','POST'])
@login_required
def enjoy_delete(id):
    from model import Enjoy,db
    query = Enjoy.query.get(id)
    db.session.delete(query)
    db.session.commit()
    return redirect('/admin/enjoy')
