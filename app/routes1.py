from  flask import redirect, url_for, render_template,request,flash, Blueprint, Flask, current_app, g
rout= Blueprint("rout",__name__,url_prefix="/")
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from app.database_function import add_db,read1_db,readall,readlast,delete_db,updatedb,autoriz_check,read1_db_email,ticket_add_db,ticket_read1_db,get_user_tickets
from app.classes import User
from app import login_manager 
import uuid

@login_manager.user_loader
def load_user(user_id):
    check_usr= read1_db(int(user_id))
    if check_usr:
        return check_usr
        
    return None



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
    return render_template('geschichte.html')

@rout.route("/uber")
def uber():
    return render_template("uber_unt.html")
@rout.route("/faq")
def faq():
    return render_template("faq.html")
@rout.route('/registration')
def registration():
    return render_template('registration.html')

@rout.route("/login_prev")
def login_prev():
    return render_template("login.html")
@rout.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('rout.haupt'))
@rout.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    if request.method == "POST":
        email = request.form.get("login_email")
        password =request.form.get('login_password')

        login_check = autoriz_check(email,password)
        if login_check:
                check_usr= read1_db_email(email)
                if check_usr:
                    login_user(check_usr)
                    return redirect(url_for('rout.haupt'))
            
    else:
        flash ("there is some problem")
        return render_template('login.html')

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
@rout.route('/profile')
@login_required
def profile():
    user_id = int(current_user.id)
    tik = get_user_tickets(user_id)
    return render_template("profile.html",tickets = tik)
@rout.route('/ticket')
@login_required
def ticket():
    
    return render_template('ticket_kaufen.html')
@rout.route('stadt_wehlen', methods=["POST"])
@login_required
def stadt_wehlen():
    uniqeid = uuid.uuid1().int %1000000
    stadt= request.form.get('town')
    ticket_add_db(stadt,uniqeid)
    return redirect(url_for('rout.profile'))

