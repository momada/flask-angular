from flask import Flask
#from flask_pymongo import PyMongo
from app.modules.user import mod_user

app = Flask(__name__)

#app.config['MONGO_URI'] = 'mongodb://localhost:27017/EventMonitor'
#mongo = PyMongo(app)

app.register_blueprint(mod_user)


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)
