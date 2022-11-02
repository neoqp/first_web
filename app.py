from flask import *
import pymysql
app= Flask(__name__)
host = '0.0.0.0'
port = '8080'


@app.route('/')
def root():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('/home.html')

@app.route('/register')
def register():
    return render_template('/register.html')

@app.route('/login')
def login():
    return render_template('/login.html')

@app.route('/pwchange')
def pwchange():
    return render_template('/pwchange.html')

@app.route('/delete')
def delete():
    return render_template('/delete.html')



@app.route('/register_confirm', methods=['POST'])
def register_confirm():
    id = request.form['id']
    pw = request.form['pw']
    
    
@app.route('/login_confirm', methods=['POST'])
def login_confirm():
    id = request.form['id']
    pw = request.form['pw']
    if id == 'admin' and pw == 'admin':
        return redirect('/index')
    else:
        return redirect('/login')

@app.route('/pwchange_confirm', methods=['POST'])
def pwchange_confirm():
    return render_template('/pwchange.html')
@app.route('/delete_confirm', methods=['POST'])
def delete_confirm():
    return render_template('/delete.html')
if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)