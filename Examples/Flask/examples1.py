#====== routing + redirecting =============================
from flask import Flask, redirect, url_for # type: ignore
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return "This is Home page"
 
@app.route('/login')
def login():
    return "This is login page"
 
@app.route('/logout')
def got_to_login():
    return redirect(url_for('login'))
 
if __name__ == '__main__':
    app.run(debug=True)