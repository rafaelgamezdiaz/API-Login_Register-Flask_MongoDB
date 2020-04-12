from flask import Flask, request, Response, jsonify
from database.db import host, initialize_db
from database.Users import User
from passlib.hash import sha256_crypt as crypt


# Init Project
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'host': host}
initialize_db(app)


@app.route('/')
def home():
    return jsonify({'message': 'This is a Login-Register API'})


@app.route('/users')
def index():
    users = User.objects().to_json()
    return Response(users, mimetype='application/json', status=200)


@app.route('/users', methods=['POST'])
def register():
    data = request.get_json()
    if data['password'] == data['password_confirm']:
        del data['password_confirm']
        try:
            user = User(name=data['name'], email=data['email'], password=crypt.encrypt(data['password'])).save()
            return {'message': 'User was created', 'id': str(user.id)}, 200
        except Exception as e:
            return jsonify({'message': 'Email or Username is used', 'error': e})
    else:
        return jsonify({'error': 'Passwords nor match'})


@app.route('/users/<id>')
def show(id):
    user = User.objects.get(id=id).to_json()
    return Response(user, mimetype="application/json", status=200)


@app.route('/users/<id>', methods=['put'])
def update(id):
    data = request.get_json()
    User.objects.get(id=id).update(**data)
    return jsonify({'message': 'User updated'}), 200


@app.route('/users/<id>', methods=['DELETE'])
def remove(id):
    try:
        User.objects.get(id=id).delete()
        return jsonify({'message': 'User was deleted'}), 200
    except Exception as e:
        return jsonify({'message': 'Error, user was not deleted'}), 409


if __name__ == '__main__':
    app.run(debug=True)
