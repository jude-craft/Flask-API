from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User(name =  {self.name}, email = {self.email})>'
    
user_args = reqparse.RequestParser()
user_args.add_argument("name", type=str, help="Name of the user is required", required=True)
user_args.add_argument("email", type=str, help="Email of the user is required", required=True)  

userFields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String
}

class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users
 
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(name=args['name'], email=args['email'])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return user, 201
    
class User(Resource):
    @marshal_with(userFields)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user
    
    @marshal_with(userFields)
    def put(self, user_id):
        args = user_args.parse_args()
        user = UserModel.query.get_or_404(user_id)
        user.name = args['name']
        user.email = args['email']
        db.session.commit()
        return user, 200
    
    @marshal_with(userFields)  
    def patch(self, user_id):
        args = user_args.parse_args()
        user = UserModel.query.get_or_404(user_id)
        if args['name']:
            user.name = args['name']
        if args['email']:
            user.email = args['email']
        db.session.commit()
        return user, 200
    

    

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 204
    
api.add_resource(Users, "/api/users")
api.add_resource(User, "/api/users/<int:user_id>")

@app.route('/home')
def home():
    return 'Welcome to the Home Page'

if __name__ == '__main__':
    app.run(debug=True)
