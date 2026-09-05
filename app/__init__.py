from flask import Flask
from flask_login import LoginManager
from app.database_function import create_admin
from dotenv import load_dotenv
import os

load_dotenv()

login_manager = LoginManager()
def create():
    app=Flask(__name__)
    app.secret_key = os.getenv('secret_key')
    login_manager.init_app(app)
    login_manager.login_view = 'rout.login'
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