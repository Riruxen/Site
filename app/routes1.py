from  flask import redirect, url_for, render_template,request,flash, Blueprint, Flask
rout= Blueprint("rout",__name__,url_prefix="/")
from flask_login import login_user, logout_user, login_required, current_user
from app.database_function import add_db,read1_db,readall,readlast,delete_db,updatedb,autoriz_check,read1_db_email,ticket_add_db,ticket_read1_db,get_user_tickets,check_admin
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

@rout.route("admin_panel")
@login_required
def admin():
    if check_admin:
        return render_template('admin_panel.html')
    else:
        return redirect(url_for('rout.haupt'))

@rout.route("/delete_admin",methods = ["POST"])
@login_required
def delete_admin():
    print(current_user.email)
    if check_admin():
        id_delete = request.form.get('id')
        delete_db(id_delete)
        flash ("Deleted")
        return render_template('admin_panel.html')
    else:
        flash("issue")
        return render_template('admin_panel.html')

@rout.route("/update_admin",methods = ["POST"])
@login_required
def update_admin():
    if check_admin():
        name_update = request.form.get('name')
        email_update = request.form.get('email')
        password_update = request.form.get('password')
        id_update = int(request.form.get('id'))
        a = {name_update,email_update,password_update,id_update}
        for i in a:
            print (i)
        if updatedb(name_update,password_update,id_update,email_update):
            flash ("update successful")
            return redirect(url_for('rout.admin'))
        else:
            flash("issue")
            return render_template('admin_panel.html')
@rout.route("/find_admin",methods = ["POST"])
@login_required
def find_admin():
    if check_admin():
        find = request.form.get('id')
        read1_db(find)
        flash ("Found one")
        return redirect(url_for('rout.admin_panel'))

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
    return render_template("innsbruck.html")
@rout.route("/geschichte")
def geschichte():
    return render_template('geschichte.html')

@rout.route("/uber")
def uber():
    return render_template("uber_uns.html")
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
