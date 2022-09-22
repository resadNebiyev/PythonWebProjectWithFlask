from flask import render_template,request,redirect,url_for
from admin import admin_bp
from werkzeug.utils import secure_filename
import os
import random
from flask_login import login_required,logout_user