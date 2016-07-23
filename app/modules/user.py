from flask import Blueprint, request
import sys
import json
from werkzeug import Response
from app import mongo
from bson import json_util

mod_user = Blueprint('user', __name__)


@mod_user.route('/api/user/authentication', methods=['POST'])
def authentication():
    user = request.json
    print >> sys.stderr, user,
    validUserCount = mongo.db.User.count({"username":user['username'],"password":user['password']})
    if validUserCount==0:
        return Response(
            'Login failed', 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'})

    result=mongo.db.User.find_one({"username":user['username'],"password":user['password']})

    return Response(json.dumps(result, default=json_util.default), mimetype='application/json')
