from flask import Flask, render_template # type: ignore
 
app = Flask(__name__)
 
@app.route('/user/<username>')
def user(username):
    return render_template('index.html',name=username)
 
if __name__ == '__main__':
    app.run(debug=True)