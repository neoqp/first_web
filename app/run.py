from flask import *
import pymysql

app= Flask(__name__)
app.secret_key=b'230&6^240)'
host = '0.0.0.0'
port = '8080'

db = pymysql.Connect(host='localhost',user='root',password='eodus6450', database='web_db')
cursor = db.cursor()

@app.route('/')
def root():
    return redirect('/home')

@app.route('/home')
def home():
    if 'id' in session:
        return render_template('/home.html',id=session['id'])
    else:
        return render_template('/home.html',id='XXX')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
        query = "INSERT INTO user (id, pw) VALUES (%s, %s)"
        data = (id,pw)
        cursor.execute(query,data)
        return redirect('/home')

    else:
        return render_template('/register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        id = request.form['id']
        session['id']=request.form['id']
        return redirect('/home')

    else:
        return render_template('/login.html')

@app.route('/pwchange')
def pwchange():
    return render_template('/pwchange.html')

@app.route('/delete')
def delete():
    return render_template('/delete.html')

    
@app.route('/login_confirm', methods=['POST'])
def login_confirm():
    id = request.form['id']
    pw = request.form['pw']
    query = "SELECT id, pw FROM user WHERE id=%s and pw=%s"
    data = (id,pw)
    cursor.execute(query,data)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)