from flask import Blueprint, request
import sys
import json
from werkzeug import Response
#from app import mongo
#from bson import json_util


mod_user = Blueprint('user', __name__)


@mod_user.route('/api/user/authentication', methods=['POST'])
def authentication():
    user = request.json
    print >> sys.stderr, user,
#    validUserCount = mongo.db.User.count({"username":user['username'],"password":user['password']})
#    if validUserCount==0:
    if (user["username"] != 'jason') | (user['password'] != 'password'):
        return Response(
            'Login failed', 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'})

    result = True

    return Response(json.dumps(result), mimetype='application/json')
