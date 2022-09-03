
from flask import render_template,request,redirect
from auth import auth_bp
from auth.form import *
@auth_bp.route('/',methods=['GET','POST'])
def index():
    return render_template('auth/index.html')

# Istifadəçilərin Admin Panelə Daxil Olması 

@auth_bp.route('/login',methods=['GET','POST'])
def login():
    loginForm = LoginForm()
    from model import Users
    if request.method=='POST':
        for user in Users.query.all():
            if user.email==loginForm.email.data and user.passward==loginForm.passward.data:
                return redirect('/admin/')
    return render_template('auth/login.html',loginForm=loginForm)

# Istifadəçilərin qeydiyyatdan keçməsi

@auth_bp.route('/register',methods=['GET','POST'])
def register():
    registerForm = RegisterForm()
    from model import Users,db
    if request.method =='POST':
        password = registerForm.passward.data
        if len(password) >=5 and len(password)<= 10:
            if any(char.isupper() for char in password):
                if any(char.islower() for char in password):
                    user = Users(name=registerForm.name.data,email=registerForm.email.data,passward = registerForm.passward.data,info=registerForm.info.data)
                    db.session.add(user)
                    db.session.commit()
                    return redirect('/auth/login')
    return render_template('auth/register.html',registerForm=registerForm)


