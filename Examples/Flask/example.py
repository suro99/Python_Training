from flask import Flask, request # type: ignore
 
app = Flask(__name__)
 
@app.route('/form',methods=['GET','POST'])
def form_examples():
    if request.method == 'POST':
        data = request.form['username']
        return f"Hello {data} , your forms is submitted !!"
    return '''
        <form method="POST">
        <input type="text" name="username">
        <input type="submit">
        </form>
'''
 
if __name__ == '__main__':
    app.run(debug=True)