from flask import render_template,request,redirect
from auth import auth_bp
from auth.form import *
from flask_login import login_user


@auth_bp.route('/',methods=['GET','POST'])
def index():
    return render_template('auth/index.html')

# Istifadəçilərin Login olunması

@auth_bp.route('/login',methods=['GET','POST'])
def login():
    from run import  bcrypt
    loginForm = LoginForm()
    from model import Users
    if request.method=='POST':
        user  = Users.query.filter_by(email=loginForm.email.data).first()
        if bcrypt.check_password_hash(user.passward,loginForm.passward.data):   
            login_user(user)
            return redirect('/admin/')
    return render_template('auth/login.html',loginForm=loginForm)

# Istifadəçilərin qeydiyyatdan keçməsi

@auth_bp.route('/register',methods=['GET','POST'])
def register():
    from run import bcrypt
    registerForm = RegisterForm()
    from model import Users,db
    users=Users.query.all()
    if request.method =='POST':
        password = registerForm.passward.data
        if len(password) >=5 and len(password)<= 10:
            if any(char.isupper() for char in password):
                if any(char.islower() for char in password):
                    pw_hash = bcrypt.generate_password_hash(password)
                    user = Users(name=registerForm.name.data,email=registerForm.email.data,passward = pw_hash,info=registerForm.info.data)
                    db.session.add(user)
                    db.session.commit()
                    return redirect('/auth/login')
    return render_template('auth/register.html',registerForm=registerForm,users=users)


@auth_bp.route('/delete/<id>',methods=['GET','POST'])
def delete(id):
    from model import Users,db
    query = Users.query.get(id)
    db.session.delete(query)
    db.session.commit()
    return redirect('/auth/register')