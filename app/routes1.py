from  flask import redirect, url_for, render_template,request,flash, Blueprint
rout= Blueprint("rout",__name__,url_prefix="/")
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
#from app.database_function import add_db,read1_db,readall,readlast,delete_db,updatedb,autoriz_check#

@rout.route("/")
def show():
    return render_template("haupt.html")