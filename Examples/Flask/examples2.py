# database connection :
 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
 
# Database Configuration
# Format: dialect+driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yourpassword@localhost:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
 
# Initialize DB
db = SQLAlchemy(app)
 
# Define Model (table)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
 
    def __repr__(self):
        return f"<User {self.name}>"
 
# Create Tables
@app.before_first_request
def create_tables():
    db.create_all()
 
# Routes
@app.route('/')
def home():
    return "Flask connected to PostgreSQL!"
 
@app.route('/add/<name>/<email>')
def add_user(name, email):
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return f"User {name} added successfully!"
 
@app.route('/users')
def get_users():
    users = User.query.all()
    return { "users": [ {"id": u.id, "name": u.name, "email": u.email} for u in users ] }
 
if __name__ == '__main__':
    app.run(debug=True)