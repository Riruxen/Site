from  flask import redirect, url_for, render_template,request,flash, Blueprint
rout= Blueprint("rout",__name__,url_prefix="/")
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from app.database_function import add_db,read1_db,readall,readlast,delete_db,updatedb,autoriz_check#

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
    return render_template("linz.html")
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

@rout.route("/uber")
def uber():
    return render_template("haupt.html")
@rout.route("/faq")
def faq():
    return render_template("haupt.html")
@rout.route('/registration')
def registration():
    return render_template('registration.html')
@rout.route("/add", methods= ["POST"])
def add():
    user = request.form.get("exampleInputname")
    email = request.form.get("exampleInputEmail1")
    password = request.form.get("exampleInputPassword1")
    if user and password and email:
        if add_db(user,password,email):
            flash("You are successfully added a user into the Flask Application")
            return redirect(url_for("rout.show"))
        
        else:
            flash("This is already busy")
            return redirect(url_for("rout.show"))
    else:
        flash("Please enter something to add!")
        return redirect(url_for("rout.show"))
