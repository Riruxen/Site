from flask import Flask
def create():
    app=Flask(__name__)
    from app.routes1 import rout
    app.secret_key = "GeeksForGeeks"
    app.register_blueprint(rout)
    return app