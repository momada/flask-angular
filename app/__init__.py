from flask import Flask, request
#from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_socketio import SocketIO, emit

app = Flask(__name__)

#app.config['MONGO_URI'] = 'mongodb://abtAdmin:abtAdmin@DV2CORP1MDB5:27117/EventMonitor'

#mongo = PyMongo(app)

db_server = 'dv2corp1mdb5:27117,dv2corp1mdb6:27117,dv2corp1mdb7:27117'
mongo_user = 'abtAdmin'
mongo_pw = 'abtAdmin'
uri = "mongodb://" + mongo_user + ":" + mongo_pw + "@" + db_server + "/?readPreference=secondary"
mongo = MongoClient(uri)


async_mode = None
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, async_mode=async_mode)

from app.modules.user import mod_user
app.register_blueprint(mod_user)

from app.modules.eventMonitor import mod_eventMonitor
app.register_blueprint(mod_eventMonitor)

from app.modules.device import mod_device
app.register_blueprint(mod_device)

@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/test')
def test():
    return "Hello World!"


@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)


@socketio.on('EventOccurred', namespace='/ws')
def event_occurred(data):
    emit('Moniter need refresh',data, broadcast=True)		