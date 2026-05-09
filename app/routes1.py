from  flask import redirect, url_for, render_template,request,flash, Blueprint
rout= Blueprint("rout",__name__,url_prefix="/")
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
#from app.database_function import add_db,read1_db,readall,readlast,delete_db,updatedb,autoriz_check#

@rout.route("/")
def show():
    return redirect("/haupt_tierschutz")
@rout.route("/haupt_tierschutz")
def haupt():
    return render_template("haupt.html")
@rout.route("/wien")
def wien():
    return render_template("wien.html")
@rout.route("/linz")
def linz():
    return render_template("haupt.html")
@rout.route("/salzburg")
def salzburg():
    return render_template("salzburg.html")
@rout.route("/graz")
def graz():
    return render_template("graz.html")
@rout.route("/inssbruck")
def inssbruck():
    return render_template("inssbruck.html")
@rout.route("/geschichte")
def geschichte():
    return render_template("haupt.html")

@rout.route("/über")
def über():
    return render_template("haupt.html")
@rout.route("/faq")
def faq():
    return render_template("haupt.html")