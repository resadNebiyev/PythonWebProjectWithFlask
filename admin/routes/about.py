from admin.routes.imports import *
@admin_bp.route('/about',methods=['GET','POST'])
def about():
    from form import AboutForm,RecommendsForm
    context = {
        'aboutForm':AboutForm(),
        'recommendsForm':RecommendsForm()
    }
    return render_template('admin/about.html',**context)
    