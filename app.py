from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity # security.py
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'leo'
api = Api(app)

# JWT creates a new endpoint: /auth, it calls the authenticate method with users
# and password and then /auth returns a JWT token
# And then the JWT token can be sent to the next requests. JWT calls the identity function
jwt = JWT(app, authenticate, identity)

# http://localhost:5000/store/<name>
api.add_resource(Store, '/store/<string:name>')

# http://localhost:5000/item/<name>
api.add_resource(Item, '/item/<string:name>')

# http://localhost:5000/stores
api.add_resource(StoreList, '/stores')

# http://localhost:5000/items
api.add_resource(ItemList, '/items')

# http://localhost:5000/register
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port = 5000, debug = True)
