from flask import Flask
from flask_login import LoginManager, UserMixin, login_user, login_required
from app.database_function import create_admin
login_manager = LoginManager()
def create():
    app=Flask(__name__)
    login_manager.init_app(app)
    login_manager.login_view = 'rout.login'
    app.secret_key = "GeeksForGeeks"
    app.login_manager = login_manager 
    from app.routes1 import rout
    @app.cli.command('create-admin')
    def create_admin_command():
        user = input("User name ")
        email = input("Admin email ")
        password = input("Password ")
        succes = create_admin(user,email,password)
        if succes:

            print(f'{email} is now admin')
        else:
            print(f'some problem was there')
    
    app.register_blueprint(rout)
    return app